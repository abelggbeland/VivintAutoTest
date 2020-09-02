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
                                "text": "The user " + str(data.getBadgeID()) + str(data.getName()) +
                                        " returned a computer asset tagged as" + str(data.getAssets()[0][1].get())
                                        + " They also returned a monitor asset tagged as " + str(data.getAssets()[1][1].get())
                                        + " returned a keyboard " + str(data.getPeripherals()[0].get())
                                        + " returned a mouse " + str(data.getPeripherals()[1].get())
                                        + " returned a headset " + str(data.getPeripherals()[2].get()),
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "assignee": {
                "accountId": str((Sender.get("https://vivint.atlassian.net/rest/api/3/myself")).json()["accountId"])
            }
        }

    })

    return payload