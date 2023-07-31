mkdir -p ./batteries && touch ./batteries/{__init__,battery,spindler_battery,nubbin_battery}.py
touch engines/engine.py
touch {serviceable,car_factory}.py

# tests
touch conftest.py
mkdir -p ./test/test_utils && touch ./test/test_utils/test_add_years_to_date.py
touch test/test_create_{calliope,glissade,palindrome,rorschach,thovex}.py

mkdir -p ./test/test_batteries && touch ./test/test_batteries/test_{spindler_battery,nubbin_battery}.py
mkdir -p ./test/test_engines && touch ./test/test_engines/test_{capulet_engine,sternman_engine,willoughby_engine}.py


