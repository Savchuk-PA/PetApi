# from pprint import pprint
#
# import requests
#
#
# headers = {"Content-Type": "application/json"}
# # endpoint = "/pet"
# # pet_data = {
# #     "id": 10,
# #     "name": "Barsik51",
# #     "category": {"id": 11, "name": "cat"},
# #     "photoUrls": ["https://example.com/photo.jpg"],
# #     "tags": [{"id": 15, "name": "big_cat"}],
# #     "status": "available",
# # }
# #
# #
# # response = requests.post(
# #     f"{host}{endpoint}",
# #     headers={"Content-Type": "application/json"},
# #     json=pet_data,
# # )
# # status_code = response.status_code
# # print(status_code)
# # assert status_code == 201, f"Ac_result: {status_code}, Ex_res: {201}"
#
# end_get = "/pet/10"
# get_response = requests.get(
#     url=f"{host}{end_get}",
#     headers=headers,
# )
# pprint(get_response.json())
