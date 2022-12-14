import marqo
import pprint

mq = marqo.Client(url='http://127.0.0.1:8882')
print("****Simple football competition search with Marqo Tensor search****")
title = input("Enter football search term\n");


mq.index("football-data").add_documents([
  {
    "competition_id": 16,
    "season_id": 4,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2018/2019",
    "match_updated": "2020-02-27T12:19:39.458017",
    "match_available": "2020-02-27T12:19:39.458017"
  },
  {
    "competition_id": 16,
    "season_id": 1,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2017/2018",
    "match_updated": "2020-06-11T01:24:40.306618",
    "match_available": "2020-06-11T01:24:40.306618"
  },
  {
    "competition_id": 16,
    "season_id": 2,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2016/2017",
    "match_updated": "2020-06-10T22:06:56.555602",
    "match_available": "2020-06-10T22:06:56.555602"
  },
  {
    "competition_id": 16,
    "season_id": 27,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2015/2016",
    "match_updated": "2020-06-10T20:02:56.22269",
    "match_available": "2020-06-10T20:02:56.22269"
  },
  {
    "competition_id": 16,
    "season_id": 26,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2014/2015",
    "match_updated": "2020-06-10T17:04:18.637515",
    "match_available": "2020-06-10T17:04:18.637515"
  },
  {
    "competition_id": 16,
    "season_id": 25,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2013/2014",
    "match_updated": "2020-06-11T15:06:38.832473",
    "match_available": "2020-06-11T15:06:38.832473"
  },
  {
    "competition_id": 16,
    "season_id": 24,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2012/2013",
    "match_updated": "2020-06-10T01:23:02.861683",
    "match_available": "2020-06-10T01:23:02.861683"
  },
  {
    "competition_id": 16,
    "season_id": 23,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2011/2012",
    "match_updated": "2020-06-09T23:06:48.094931",
    "match_available": "2020-06-09T23:06:48.094931"
  },
  {
    "competition_id": 16,
    "season_id": 22,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2010/2011",
    "match_updated": "2020-06-09T19:25:59.629616",
    "match_available": "2020-06-09T19:25:59.629616"
  },
  {
    "competition_id": 16,
    "season_id": 21,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2009/2010",
    "match_updated": "2020-06-09T17:04:26.558849",
    "match_available": "2020-06-09T17:04:26.558849"
  },
  {
    "competition_id": 16,
    "season_id": 41,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2008/2009",
    "match_updated": "2020-06-08T17:37:13.057374",
    "match_available": "2020-06-08T17:37:13.057374"
  },
  {
    "competition_id": 16,
    "season_id": 39,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2006/2007",
    "match_updated": "2020-06-08T23:15:00.015201",
    "match_available": "2020-06-08T23:15:00.015201"
  },
  {
    "competition_id": 16,
    "season_id": 37,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2004/2005",
    "match_updated": "2020-06-08T15:38:30.853093",
    "match_available": "2020-06-08T15:38:30.853093"
  },
  {
    "competition_id": 16,
    "season_id": 44,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "2003/2004",
    "match_updated": "2020-06-06T16:04:33.453344",
    "match_available": "2020-06-06T16:04:33.453344"
  },
  {
    "competition_id": 16,
    "season_id": 76,
    "country_name": "Europe",
    "competition_name": "Champions League",
    "competition_gender": "male",
    "season_name": "1999/2000",
    "match_updated": "2020-04-03T08:44:23.412603",
    "match_available": "2020-04-03T08:44:23.412603"
  },
  {
    "competition_id": 37,
    "season_id": 42,
    "country_name": "England",
    "competition_name": "FA Women's Super League",
    "competition_gender": "female",
    "season_name": "2019/2020",
    "match_updated": "2020-06-21T13:15:27.139235",
    "match_available": "2020-06-21T13:15:27.139235"
  },
  {
    "competition_id": 37,
    "season_id": 4,
    "country_name": "England",
    "competition_name": "FA Women's Super League",
    "competition_gender": "female",
    "season_name": "2018/2019",
    "match_updated": "2020-04-23T19:04:49.880742",
    "match_available": "2020-04-23T19:04:49.880742"
  },
  {
    "competition_id": 43,
    "season_id": 3,
    "country_name": "International",
    "competition_name": "FIFA World Cup",
    "competition_gender": "male",
    "season_name": "2018",
    "match_updated": "2019-12-16T23:09:16.168756",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 11,
    "season_id": 4,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2018/2019",
    "match_updated": "2020-04-21T21:40:19.168478",
    "match_available": "2020-04-21T21:40:19.168478"
  },
  {
    "competition_id": 11,
    "season_id": 1,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2017/2018",
    "match_updated": "2020-05-03T17:05:26.772937",
    "match_available": "2020-05-03T17:05:26.772937"
  },
  {
    "competition_id": 11,
    "season_id": 2,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2016/2017",
    "match_updated": "2020-06-21T21:11:44.983975",
    "match_available": "2020-06-21T21:11:44.983975"
  },
  {
    "competition_id": 11,
    "season_id": 27,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2015/2016",
    "match_updated": "2020-04-13T23:02:59.803428",
    "match_available": "2020-04-13T23:02:59.803428"
  },
  {
    "competition_id": 11,
    "season_id": 26,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2014/2015",
    "match_updated": "2019-12-16T23:09:16.168756",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 11,
    "season_id": 25,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2013/2014",
    "match_updated": "2019-12-16T23:09:16.168756",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 11,
    "season_id": 24,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2012/2013",
    "match_updated": "2020-04-13T23:02:59.803428",
    "match_available": "2020-04-13T23:02:59.803428"
  },
  {
    "competition_id": 11,
    "season_id": 23,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2011/2012",
    "match_updated": "2020-04-13T23:02:59.803428",
    "match_available": "2020-04-13T23:02:59.803428"
  },
  {
    "competition_id": 11,
    "season_id": 22,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2010/2011",
    "match_updated": "2020-04-09T13:13:49.345111",
    "match_available": "2020-04-09T13:13:49.345111"
  },
  {
    "competition_id": 11,
    "season_id": 21,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2009/2010",
    "match_updated": "2019-12-16T23:09:16.168756",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 11,
    "season_id": 41,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2008/2009",
    "match_updated": "2019-12-16T23:09:16.168756",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 11,
    "season_id": 40,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2007/2008",
    "match_updated": "2019-12-16T23:09:16.168756",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 11,
    "season_id": 39,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2006/2007",
    "match_updated": "2019-12-16T23:09:16.168756",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 11,
    "season_id": 38,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2005/2006",
    "match_updated": "2020-02-27T12:19:39.458017",
    "match_available": "2020-02-27T12:19:39.458017"
  },
  {
    "competition_id": 11,
    "season_id": 37,
    "country_name": "Spain",
    "competition_name": "La Liga",
    "competition_gender": "male",
    "season_name": "2004/2005",
    "match_updated": "2019-12-16T23:09:16.168756",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 49,
    "season_id": 3,
    "country_name": "United States of America",
    "competition_name": "NWSL",
    "competition_gender": "female",
    "season_name": "2018",
    "match_updated": "2020-02-27T15:22:21.167136",
    "match_available": "2019-12-16T23:09:16.168756"
  },
  {
    "competition_id": 2,
    "season_id": 44,
    "country_name": "England",
    "competition_name": "Premier League",
    "competition_gender": "male",
    "season_name": "2003/2004",
    "match_updated": "2020-06-21T23:24:17.606581",
    "match_available": "2020-06-21T23:24:17.606581"
  },
  {
    "competition_id": 72,
    "season_id": 30,
    "country_name": "International",
    "competition_name": "Women's World Cup",
    "competition_gender": "female",
    "season_name": "2019",
    "match_updated": "2020-02-27T12:19:39.458017",
    "match_available": "2020-02-27T12:19:39.458017"
  }
])

results = mq.index("football-data").search(q=title)

pprint.pprint(results)
