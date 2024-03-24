
request={
    "header":{
        "usertype": "patient",
        "datetime": "YY/MM/DD",
        "version": "0.1.0",
        "request" : "login"
    },
    "body":{
        "name":"김나은",
        "guardNumber": "01030236298",
        "patientNumber":"01011235677",
        "address":"대구광역시",
        "id":"adfadf",
        "pw":"dafdsfa",
        "xAddress":"133.214",
        "yAddress":"123.124"
    }
}

response={
    "header":{
        "usertype": "patient",
        "datetime": "YY/MM/DD",
        "version": "0.1.0",
        "request" : "login"
    },
    "body":{
        "name":"김나은",
        "address":"대구광역시",
        "guardNumber": "01030236298",
        "picture": ".url",
        "xAddress":"133.214",
        "yAddress":"123.124",
        "check":"check",
        "state":"login",
        "detail":"오류"
    }
}