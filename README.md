# malupdate
Unofficial Python client wrapper for v2 MyAnimeList API using the Unoffical Specification of the Official API by <br>
https://github.com/SuperMarcus/myanimelist-api-specification <br>
~~This is most likely temporary till the time I can get beta access to MAL's API or they release it to the public.~~ <br>
As of July 2020, MAL has made their API public and any changes and updates done to this project will be in reference to the official documentation of the API.

## Installation
PyPi: https://pypi.org/project/malupdate/ <br>
`pip install malupdate`
## Usage
### `Class User`:
* **`User.login(username, password):`** Takes in username and password of MAL account as arguments and returns a loginObject (dictionary) consisting of keys `access_token`, `expires_in`, `refresh_token`.

* **`User.myInfo(Access_Token, [field_1, field_2, ...]):`** Returns User Profile information and statistics (if `anime_statistics` field is used as argument).

* **`User.getAnimeList(Access_Token, type_of_list, [field_1, field_2, ....]):`** Takes the `access_token` from the loginObject, the type of list (`watching`/ `plan_to_watch`/ `completed`/ `on_hold`/ `dropped`) and one or more [fields](https://github.com/SuperMarcus/myanimelist-api-specification#response-objects) as a list. Returns a JSON object (dictionary) of shows in the list.

* **`User.updateList(Access_Token, show_id, {field_1: val_1, field_2: val_2 ...}):`** Takes the `access_token` from the loginObject, `id` of the show to be updated, a list of [fields](https://github.com/SuperMarcus/myanimelist-api-specification#response-objects) which are to be updated and their corresponding new values in dictionary form. <br>
Returns a JSON object (dictionary) of user's list with updated values.

* **`User.deleteItem(Access_Token, anime_id):`** Takes in `id` of an anime and removes it from the User's list.

### `Class Anime`:
* **`Anime.search(Access_Token, anime_name, [field_1, field_2, ...]):`** Takes the `access_token`, name of the anime and the [fields](https://github.com/SuperMarcus/myanimelist-api-specification#response-objects) to be displayed as arguments. Returns a JSON object (dictionary) of search results. <br>

* **`Anime.bySeason(Access_Token, year, season, [field_1, field_2, ...], sort="", limit=100, offset=0, nsfw=False):`** Takes year and season (`winter`/ `spring`/ `summer` /`fall`) as required arguments and returns a JSON object of the anime list. List can be sorted based on `anime_score` or `anime_num_list_users` in descending. By default, NSFW results are filtered out but can be enabled by setting `nsfw` parameter as `True`.

* **`Anime.byRanking(Access_Token, ranking_type, [field_1, field_2, ...], limit=100, offset=0, nsfw=False):`** Takes in a `ranking_type` (`all`/ `airing`/ `upcoming`/ `tv`/ `ova`/ `movie`/ `special`/ `bypopularity`/ `favorite`) and returns a JSON object of the anime list. NSFW can be turned on with `nsfw` parameter set to `True`.

## Things to Improve
* Better support for pagination.
* Possible design changes to make it more developer friendly.

## Projects that use malupdate
* [Umaru-chan](https://github.com/m0mosenpai/Umaru-chan)

## License
MIT
