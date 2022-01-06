## Meetup-YourFirstEventDrivenApp

NJ Meetup - Build an event-driven architecture with Apache Pulsar

### Code Along

````

bin/pulsar-admin tenants create meetup
bin/pulsar-admin namespaces create meetup/newjersey
bin/pulsar-admin tenants list 
bin/pulsar-admin namespaces list meetup
bin/pulsar-admin topics create persistent://meetup/newjersey/first
bin/pulsar-admin topics list meetup/newjersey

bin/pulsar-client consume "persistent://meetup/newjersey/first" -s first-reader -n 0

````

### Pulsar SQL Code Along

````
bin/pulsar sql

show catalogs;
show schemas in pulsar;
show tables in pulsar."meetup/newjersey";
describe pulsar."meetup/newjersey"."first";

select * from pulsar."meetup/newjersey"."first";

select __key__, from_utf8(__value__), 
           __publish_time__, __message_id__,
           __producer_name__
from pulsar."meetup/newjersey"."first"
order by __publish_time__ desc;

exit;

````

### Monitoring Code Along

````
curl http://localhost:8080/admin/v2/persistent/meetup/newjersey/first/stats | python3 -m json.tool

bin/pulsar-admin topics stats-internal persistent://meetup/newjersey/first

curl http://pulsar1:8080/metrics/

bin/pulsar-admin topics stats-internal persistent://meetup/newjersey/first

bin/pulsar-admin topics peek-messages --count 5 --subscription mqtt-reader persistent://meetup/newjersey/first

bin/pulsar-admin topics subscriptions persistent://meetup/newjersey/first

````

### Cleanup This Exercise (You don't have to)

````
bin/pulsar-admin topics delete persistent://meetup/newjersey/first
bin/pulsar-admin namespaces delete meetup/newjersey
bin/pulsar-admin tenants delete meetup

````

### Web Pages For Viewing

* http://pulsar1:8081/ui/
* http://pulsar1:8080/admin/v2/persistent/meetup/newjersey
* http://pulsar1:9527/#/management/topics/persistent/meetup/newjersey/first/topic?tab=storage&cluster=standalone

### References

* https://www.meetup.com/new-york-city-apache-pulsar-meetup/events/282270385/
* https://streamnative.io/event/meetup-build-an-event-driven-architecture-with-apache-pulsar/
* https://github.com/tspannhw/pulsar-adafruit-funhouse
* https://github.com/tspannhw/ScyllaFLiPSTheStream
* https://github.com/apache/pulsar-manager
