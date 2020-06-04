# malupdate
Python Package to interact with MyAnimeList using the Unoffical Specification of the Official API by <br>
https://github.com/SuperMarcus/myanimelist-api-specification <br>
This is most likely temporary till the time I can get beta access to MAL's API or they release it to the public.

## Installation
PyPi: https://pypi.org/project/malupdate/ <br>
`pip install malupdate`
## Usage
### `Class User`:
* **`User.login(username, password):`** Takes in username and password of MAL account as arguments and returns a loginObject (dictionary) consisting of keys `access_token`, `expires_in`, `refresh_token`.

* **`User.getAnimeList(Access_Token, type_of_list, [field_1, field_2, ....]):`** Takes the `access_token` from the loginObject, the type of list (`watching`/ `plan_to_watch`/ `completed`/ `on_hold`/ `dropped`) and one or more [fields](https://github.com/SuperMarcus/myanimelist-api-specification#response-objects) as a list. Returns a JSON object (dictionary) of shows in the list.

* **`User.updateList(Access_Token, show_id, {field_1: val_1, field_2: val_2 ...}):`** Takes the `access_token` from the loginObject, `id` of the show to be updated, a list of [fields](https://github.com/SuperMarcus/myanimelist-api-specification#response-objects) which are to be updated and their corresponding new values in dictionary form. <br>
Returns a JSON object (dictionary) of user's list with updated values.

### `Class Anime`:
* **`Anime.search(Access_Token, anime_name, [field_1, field_2, ...]):`** Takes the `access_token`, name of the anime and the [fields](https://github.com/SuperMarcus/myanimelist-api-specification#response-objects) to be displayed as arguments. Returns a JSON object (dictionary) of search results. <br>
NSFW Results are filtered out by default (Don't know of any way around this as of now). However, if the NSFW Title is already in your anime list, it is shown by `User.getAnimeList()`.

## Projects that use malupdate
* [Umaru-chan](https://github.com/m0mosenpai/Umaru-chan)

## License
MIT
