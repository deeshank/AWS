
import urllib
import hmac
import hashlib
import base64
import datetime
import requests

def nw():
	timestamp_datetime = datetime.datetime.utcnow()
	timestamp_list = list(timestamp_datetime.timetuple())
	timestamp_list[6] = 0
	timestamp_tuple = tuple(timestamp_list)
	return timestamp_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

ACCESSID = "ACCESSKEY"
SECRET = "SECRET_KEY"

params = { "Service":"AWSECommerceService",
	   "AssociateTag":"scanlifedev-20",
	   "Version":"2011-08-01",
	   "Condition":"All",
	   "MerchantId":"Amazon",
	   "IdType":"UPC",
	   "SearchIndex":"All",
	   "ReviewSort":"-HelpfulVotes",
	   "ResponseGroup":"Small,Images,EditorialReview,ItemAttributes,OfferSummary,Reviews,Similarities,Tracks,Accessories,OfferFull",
	   "Operation":"ItemLookup",
	   "AWSAccessKeyId": ACCESSID,
	   "ItemId":"680666600129",
	   "Timestamp":nw()
}

p=urllib.urlencode(sorted(params.items()))


MSG = """GET
ecs.amazonaws.com
/onca/xml
""" + p

URI = "http://ecs.amazonaws.com/onca/xml"

SIGN = urllib.urlencode({"Signature":base64.b64encode(hmac.new(SECRET, msg=MSG, digestmod=hashlib.sha256).digest())})

url = URI+"?"+p+"&"+SIGN

op = requests.get(url)

print op.text
