import json
import Sender

def makeIssue(data):
    payload = json.dumps({
        "fields": {
            "issuetype": {
                "name": "DS: Internal"
            },
            "project": {
                "key": "DS"
            },
            "summary": "This is a test " + "User " + str(data.getBadgeID()) + " returned",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": "The user " + str(data.getBadgeID()) + " returned " + str(
                                    data.getAssets()) + " They also returned " + str(data.getPeripherals()),
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "assignee": {
                "accountId": str((Sender.get("https://vivint.atlassian.net/rest/api/3/myself"))["accountId"])
            }
        }

    })

    return payload