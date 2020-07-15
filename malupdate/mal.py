import requests

# Constant request headers
REQUEST_HEADERS = {
	"Host": "api.myanimelist.net",
	"Accept": "application/json",
	"Content-Type": "application/x-www-form-urlencoded",
	"X-MAL-Client-ID": "6114d00ca681b7701d1e15fe11a4987e",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

class User:
	def login(user, passwd):
		URL = "https://api.myanimelist.net/v2/auth/token"
		headers= {
		    "Host": "api.myanimelist.net",
		    "Accept": "application/json",
		    "Content-Type": "application/x-www-form-urlencoded",
		    "X-MAL-Client-ID": "6114d00ca681b7701d1e15fe11a4987e",
		    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
		    "Content-Length": "112",
		}
		data = "grant_type=password&client_id=6114d00ca681b7701d1e15fe11a4987e&password={}&username={}".format(passwd, user)

		loginData = requests.post(URL, data = data, headers= headers).json()
		return loginData

	# Re-authenticate session if Access Token expires (30 Days)
	# Probably won't need this in most use cases
	def reAuthenticate(refreshToken):
		URL = "https://myanimelist.net/v1/oauth2/token"
		headers= {
		    "Host": "myanimelist.net",
		    "Accept": "application/json",
		    "Content-Type": "application/x-www-form-urlencoded",
		    "X-MAL-Client-ID": "6114d00ca681b7701d1e15fe11a4987e",
		    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
		    "Content-Length": "88",
		}
		data = "client_id=6114d00ca681b7701d1e15fe11a4987e&grant_type=refresh_token&refresh_token={}".format(refreshToken)

		loginData = requests.post(URL, data = data, headers = headers).json()
		return loginData

	# Endpoint: /users/@me
	# Get User's personal statistics
	# fields can be: [anime_statistics] (only known field as of this version)
	def myInfo(ACCESS_TOKEN, fields=[]):
		if not fields:
			URL = "https://api.myanimelist.net/v2/users/@me"
		else:
			query = "?fields="
			for field in fields:
				query += (field + ",")
			URL = "https://api.myanimelist.net/v2/users/@me" + query[:-1]

		headers = REQUEST_HEADERS
		headers["Authorization"] = "Bearer {}".format(ACCESS_TOKEN)

		stats = requests.get(URL, headers = headers).json()
		return stats

	# Endpoint: /users/{user_name}/animelist
	# where {user_name} can be @me for user's own list
	# Gets user's watchlist - status can be [watching, completed, on_hold, dropped, plan_to_watch]
	# sort can have [list_score, list_updated_at, anime_title, anime_start_date]
	def getAnimeList(ACCESS_TOKEN, status, fields=[], sort="", limit=100, offset=0):
		if not fields:
			URL = "https://api.myanimelist.net/v2/users/@me/animelist?status={}&limit={}&offset={}&sort={}".format(status, limit, offset, sort)
		else:
			query = "&fields="
			for field in fields:
				query += (field + ",")
			URL = "https://api.myanimelist.net/v2/users/@me/animelist?status={}&limit={}&offset={}&sort={}".format(status, limit, offset, sort) + query[:-1]

		headers = REQUEST_HEADERS
		headers["Authorization"] = "Bearer {}".format(ACCESS_TOKEN)
		response = requests.get(URL, headers = headers).json()
		nextPage = response['paging']

		# While the next field in response is not empty, keep sending request for next page
		animeList = [response]
		while 'next' in nextPage:
			nextURL = nextPage['next']
			nextResponse = requests.get(nextURL, headers = headers).json()
			animeList.append(nextResponse)
			nextPage = nextResponse['paging']
		return animeList

	# Endpoint: /anime/{anime_id}/my_list_status
	# Changes values of fields as per arguments
	def updateList(ACCESS_TOKEN, id, fields):		
		URL = "https://api.myanimelist.net/v2/anime/{}/my_list_status".format(id)

		headers = REQUEST_HEADERS
		headers["Authorization"] = "Bearer {}".format(ACCESS_TOKEN)

		data = ""
		for key in fields.keys():
			data += "{}={}&".format(key, fields[key])
			
		updatedList = requests.put(URL, data = data[:-1], headers = headers).json()

		return updatedList

	# Endpoint: /anime/{anime_id}/my_list_status
	# Removes an item from the User's list
	def deleteItem(ACCESS_TOKEN, id):
		URL = "https://api.myanimelist.net/v2/anime/{}/my_list_status".format(id)

		headers = REQUEST_HEADERS
		headers["Authorization"] = "Bearer {}".format(ACCESS_TOKEN)

		requests.delete(URL, headers = headers).json()

# General Anime class to search and find anime
class Anime:
	# Endpoint: /anime
	# Search anime in search field of MAL
	def search(ACCESS_TOKEN, aname, fields=[], nsfw=False):
		aname = aname.replace(' ', '+')
		if not fields:
			URL = "https://api.myanimelist.net/v2/anime?q={}&nsfw={}".format(aname, nsfw)
		else:
			query = "&fields="
			for field in fields:
				query += (field + ",")
			URL = "https://api.myanimelist.net/v2/anime?q={}&nsfw={}".format(aname, nsfw) + query[:-1]
			URL += query

		headers = REQUEST_HEADERS
		headers["Authorization"] = "Bearer {}".format(ACCESS_TOKEN)

		searchResults = requests.get(URL, headers = headers).json()
		return searchResults

	# Endpoint: /anime/ranking
	# Get anime rankings based on following ranking types:
	# [all, airing, upcoming, tv, ova, movie, special, bypopularity, favorite]
	def byRanking(ACCESS_TOKEN, ranking_type, fields=[], limit=100, offset=0, nsfw=False):
		if not fields:
			URL = "https://api.myanimelist.net/v2/anime/ranking?ranking_type={}&limit={}&offset={}&nsfw={}".format(ranking_type, limit, offset, nsfw)
		else:
			query = "&fields="
			for field in fields:
				query += (field + ",")
			URL = "https://api.myanimelist.net/v2/anime/ranking?ranking_type={}&limit={}&offset={}&nsfw={}".format(ranking_type, limit, offset, nsfw) + query[:-1]
			URL += query

		headers = REQUEST_HEADERS
		headers["Authorization"] = "Bearer {}".format(ACCESS_TOKEN)

		rankings = requests.get(URL, headers = headers).json()
		return rankings

	# Endpoint: /anime/season/{year}/{season}
	# Seasons can be: [winter, spring, summer, fall]
	# Get seasonal anime and sort in descending based on:
	# [anime_score, anime_num_list_users]
	def bySeason(ACCESS_TOKEN, year, season, fields=[], sort="", limit=100, offset=0, nsfw=False):
		if not fields:
			URL = "https://api.myanimelist.net/v2/anime/season/{}/{}?sort={}&limit={}&offset={}&nsfw={}".format(year, season, sort, limit, offset, nsfw)
		else:
			query = "&fields="
			for field in fields:
				query += (field + ",")
			URL = "https://api.myanimelist.net/v2/anime/season/{}/{}?sort={}&limit={}&offset={}&nsfw={}".format(year, season, sort, limit, offset, nsfw) + query[:-1]
			URL += query

		headers = REQUEST_HEADERS
		headers["Authorization"] = "Bearer {}".format(ACCESS_TOKEN)

		seasonal = requests.get(URL, headers = headers).json()
		return seasonal

	# Endpoint: /anime/suggestions
	# Get suggested anime based on my list
	# (Empty list is returned for new user)
	def suggested(ACCESS_TOKEN, fields=[], limit=100, offset=0, nsfw=False):
		if not fields:
			URL = "https://api.myanimelist.net/v2/anime/suggestions?limit={}&offset={}&nsfw={}".format(limit, offset, nsfw)
		else:
			query = "&fields="
			for field in fields:
				query += (field + ",")
			URL = "https://api.myanimelist.net/v2/anime/suggestions?limit={}&offset={}".format(limit, offset, nsfw) + query[:-1]
			URL += query

		headers = REQUEST_HEADERS
		headers["Authorization"] = "Bearer {}".format(ACCESS_TOKEN)

		suggested = requests.get(URL, headers = headers).json()
		return suggested