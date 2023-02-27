



from pathlib import Path
import requests

from downloadfile import downloadfile
from donwloadfilePdf import donwloadfilePdf
from OpMySql import OpMySql
mysql = OpMySql()

data =mysql.get_row("ehkaam_main", ["UploadFile"], [0])
print("download files :"+str(len(data)))
for y in data :
    my_file = Path("files/image_" + str(y["requestId"]) + ".jpg")
    if my_file.is_file()==False:
        print( ">> upload file :  " + str(y["requestId"]))


        d = downloadfile(
            "https://api.ehkaam.sa/api/app/realEstateOwnershipRequest/downloadRealestateLimitsAttachment/" + str(
                y["requestId"]), y["requestId"])
        d.getHeader()
        d = donwloadfilePdf(
            "https://api.ehkaam.sa/api/app/realEstateOwnershipRequest/downloadArealReportAttachment/" + str(
                y["requestId"]), y["requestId"])
        d.getHeader()
        mysql.up_row("ehkaam_main", ["UploadFile"], [1], ["requestId"], [y["requestId"]])


    else:
        mysql.up_row("ehkaam_main", ["UploadFile"], [1], ["requestId"], [y["requestId"]])



# counter=14
#
# #126227
# total=0
# for x in range(counter):
#     mysql = OpMySql()
#
#     url = 'https://api.ehkaam.sa/api/app/adsAppServices/adsList?skipCount='+str(total)+'&maxResultCount=1000'
#     total = total + 1000
#     resp = requests.get(url=url)
#     json = resp.json()
#
#     for y in json["items"] :
#
#
#
#         #https://api.ehkaam.sa/api/app/realEstateOwnershipRequest/downloadArealReportAttachment/77960
#
#
#
#
#
#
#         if len(mysql.get_row("ehkaam_main", ["requestId"], [y["requestId"]])) == 0:
#             print(str(total) + ">>" + str(y["requestId"]))
#             arr_main_name = ['requestId', 'area', 'realEstateType', 'cityName', 'regionName', 'publishingDate',
#                              'adsEndDate', 'remainingTime', 'remainingDays', 'latitude', 'longitude', 'ownerName']
#             arr_main_value = [y["requestId"], y["area"], y["realEstateType"], y["cityName"], y["regionName"],
#                               y["publishingDate"], y["adsEndDate"], y["remainingTime"], y["remainingDays"],
#                               y["latitude"], y["longitude"], y["ownerName"]]
#             Id_main = mysql.add_row_single("ehkaam_main", arr_main_name, arr_main_value)
#             if Id_main != 0 :
#                 print("-----")
#                 d = downloadfile(
#                     "https://api.ehkaam.sa/api/app/realEstateOwnershipRequest/downloadRealestateLimitsAttachment/"+str(
#                         y["requestId"]), y["requestId"])
#                 d.getHeader()
#                 d = donwloadfilePdf(
#                     "https://api.ehkaam.sa/api/app/realEstateOwnershipRequest/downloadArealReportAttachment/" + str(
#                         y["requestId"]), y["requestId"])
#                 d.getHeader()
#         else:
#             my_file = Path("files/image_"+str(y["requestId"])+".jpg")
#             if my_file.is_file()==False:
#                 print(str(total) + ">> upload file :  " + str(y["requestId"]))
#                 print("-----")
#                 d = downloadfile(
#                     "https://api.ehkaam.sa/api/app/realEstateOwnershipRequest/downloadRealestateLimitsAttachment/" + str(
#                         y["requestId"]), y["requestId"])
#                 d.getHeader()
#                 d = donwloadfilePdf(
#                     "https://api.ehkaam.sa/api/app/realEstateOwnershipRequest/downloadArealReportAttachment/" + str(
#                         y["requestId"]), y["requestId"])
#                 d.getHeader()
#
#
#
# print(counter)
