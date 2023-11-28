import grequests
import json

API="https://api.tzkt.io"

if __name__ == "__main__":
    
    rs = []
    rs.append(grequests.get(API+"/v1/protocols/current"))
    rs.append(grequests.get(API+"/v1/blocks/count"))

    responses = grequests.map(rs)

    if json.loads(responses[0].content).get("lastLevel") is not None:
        print("protocol finishes at block : " + str(json.loads(responses[0].content)["lastLevel"]))
    else:
        print("No protocol update staged yet")

    print("current block count : " + responses[1].content.decode())
