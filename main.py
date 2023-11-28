import grequests
import json
import sys

API="https://api.tzkt.io"


def get_API():
    rs = []
    rs.append(grequests.get(API+"/v1/protocols/current"))
    if("--show-current" in sys.argv):
        rs.append(grequests.get(API+"/v1/blocks/count"))
    return grequests.map(rs)

def display(responses):
    if json.loads(responses[0].content).get("lastLevel") is not None:
        print("proto finishes at block : " + str(json.loads(responses[0].content)["lastLevel"]))
    else:
        print("No protocol update staged yet")
        
    if("--show-current" in sys.argv):
        print("current block count : " + responses[1].content.decode())

if __name__ == "__main__":
    
    display(get_API())
