# encoding: utf-8
from __future__ import print_function

from aliyun.log import *
import time
import os

dashboard_detail = {
  "charts": [
    {
      "display": {
        "displayName": "",
        "height": 5,
        "width": 5,
        "xAxis": [
          "province"
        ],
        "xPos": 0,
        "yAxis": [
          "pv"
        ],
        "yPos": 0
      },
      "search": {
        "end": "now",
        "logstore": "access-log",
        "query": "method:  GET  | select  ip_to_province(remote_addr) as province , count(1) as pv group by province order by pv desc ",
        "start": "-86400s",
        "topic": ""
      },
      "title": "map",
      "type": "map"
    },
    {
      "display": {
        "displayName": "",
        "height": 5,
        "width": 5,
        "xAxis": [
          "province"
        ],
        "xPos": 5,
        "yAxis": [
          "pv"
        ],
        "yPos": 0
      },
      "search": {
        "end": "now",
        "logstore": "access-log",
        "query": "method:  POST  | select  ip_to_province(remote_addr) as province , count(1) as pv group by province order by pv desc ",
        "start": "-86400s",
        "topic": ""
      },
      "title": "post_map",
      "type": "map"
    }
  ],
  "dashboardName": 'alert_' + str(time.time()).replace('.', '-'),
  "description": ""
}

alert_detail = {
  "actionDetail": {
    "message": "xxxxxxx simple test"
  },
  "actionType": "notification",
  "alertDetail": {
    "alertKey": "f2",
    "alertValue": "200",
    "comparator": ">"
  },
  "checkInterval": 5,
  "count": 10,
  "from": "-300s",
  "roleArn": "acs:ram::1654218965343050:role/aliyunlogreadrole",
  "savedsearchName": "quck-query-all",
  "to": "now",
  "alertName": 'alert_' + str(time.time()).replace('.', '-')
}

savedsearch_detail = {
    "logstore": "test2",
    "savedsearchName": 'search_' + str(time.time()).replace('.', '-'),
    "searchQuery": "boy | select sex, count() as Count group by sex",
    "topic": ""
}


def main():
    endpoint = os.environ.get('ALIYUN_LOG_SAMPLE_ENDPOINT', '')
    accessKeyId = os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSID', '')
    accessKey = os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSKEY', '')
    project = os.environ.get('ALIYUN_LOG_SAMPLE_PROJECT', '')

    dashboard = dashboard_detail.get('dashboardName')

    client = LogClient(endpoint, accessKeyId, accessKey, "")

    res = client.create_dashboard(project, dashboard_detail)
    res.log_print()

    res = client.list_dashboard(project)
    res.log_print()

    res = client.get_dashboard(project, dashboard)
    res.log_print()

    res = client.update_dashboard(project, dashboard_detail)
    res.log_print()

    res = client.delete_dashboard(project, dashboard)
    res.log_print()


    alert = alert_detail.get('alertName')

    res = client.create_alert(project, alert_detail)
    res.log_print()

    res = client.list_alert(project)
    res.log_print()
    print(res.get_alerts())

    res = client.get_alert(project, alert)
    res.log_print()

    res = client.update_alert(project, alert_detail)
    res.log_print()

    res = client.delete_alert(project, alert)
    res.log_print()

    savedsearch = savedsearch_detail.get('savedsearchName')

    res = client.create_savedsearch(project, savedsearch_detail)
    res.log_print()

    res = client.list_savedsearch(project)
    res.log_print()
    print(res.get_savedsearches())

    res = client.get_savedsearch(project, savedsearch)
    res.log_print()

    res = client.update_savedsearch(project, savedsearch_detail)
    res.log_print()

    res = client.delete_savedsearch(project, savedsearch)
    res.log_print()


if __name__ == '__main__':
    main()


