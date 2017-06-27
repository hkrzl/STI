Hakim Razalee [IPMI Poller && IBMS]

============Rack-HD Token============================

GET-TOKEN:

curl -u admin:admin http://localhost:5000/rackhd/login -d '{"username":"admin","password":"admin123"}' -H "Content-Type: application/json" -X POST | python -m json.tool

=====================IPMI POLLER============================

IPMI CREATE:

curl -u admin:admin http://localhost:5000/rackhd/ipmipollers/create -d '{"type":"ipmi","node":"54daadd764f1a8f1088fdc42","command":"power"}' -H "Content-type: application/json" -X POST -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTgwMTY2NDAsImV4cCI6MTQ5ODEwMzA0MH0.CRCsEGp4Hb_mFYykWgmsN6CuaCtfBbzgOUv09C-_HLA ' | python -m json.tool

IPMI READ:

curl -u admin:admin http://localhost:5000/rackhd/ipmipollers/read -X GET -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTgwMTY2NDAsImV4cCI6MTQ5ODEwMzA0MH0.CRCsEGp4Hb_mFYykWgmsN6CuaCtfBbzgOUv09C-_HLA ' | python -m json.tool

IPMI UPDATE:

curl -u admin:admin http://localhost:5000/rackhd/ipmipollers/update -d '{"pid":"59495d5004a9f71405c06eec", "paused":"true","pollInterval":"10000"}' -H "Content-type: application/json" -X PATCH -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTgwMTY2NDAsImV4cCI6MTQ5ODEwMzA0MH0.CRCsEGp4Hb_mFYykWgmsN6CuaCtfBbzgOUv09C-_HLA ' | python -m json.tool

IPMI DELETE:

curl -u admin:admin http://localhost:5000/rackhd/ipmipollers/delete -d '{"pid":" "}' -X DELETE -H "Content-type: application/json" -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTgwMTY2NDAsImV4cCI6MTQ5ODEwMzA0MH0.CRCsEGp4Hb_mFYykWgmsN6CuaCtfBbzgOUv09C-_HLA '

============IBMS============================

IBMS CREATE:

curl -u admin:admin http://localhost:5000/rackhd/ibms/create -d '{"id":"591c569c087752c67428e4b3","nodeId":"590cbcbf29ba9e40471c9f3c","service":"snmp-ibm-service","community":"public","host":"172.31.128.2"}' -H "Content-type: application/json" -X PUT -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc5Nzg0MDQsImV4cCI6MTQ5ODA2NDgwNH0.TVxOtIbMwyQfkAaOnVPcoLCQopoM2tC3fcS7LbHJuGg' | python -m json.tool

IBMS READ:

curl -u admin:admin http://localhost:5000/rackhd/ibms/read -X GET -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc5Nzg0MDQsImV4cCI6MTQ5ODA2NDgwNH0.TVxOtIbMwyQfkAaOnVPcoLCQopoM2tC3fcS7LbHJuGg' | python -m json.tool

IBMS UPDATE:

curl -u admin:admin http://localhost:5000/rackhd/ibms/update -d '{"id":"5949f7f604a9f71405c06ef5","service":"snmp-ibm-service","community":"public","host":"172.31.128.198"}' -H "Content-type: application/json" -X PATCH -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc5Nzg0MDQsImV4cCI6MTQ5ODA2NDgwNH0.TVxOtIbMwyQfkAaOnVPcoLCQopoM2tC3fcS7LbHJuGg' | python -m json.tool

IBMS DELETE:

curl -u admin:admin http://localhost:5000/rackhd/ibms/delete -d '{"id":”5949f7f604a9f71405c06ef5"}' -X DELETE -H "Content-type: application/json" -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc5Nzg0MDQsImV4cCI6MTQ5ODA2NDgwNH0.TVxOtIbMwyQfkAaOnVPcoLCQopoM2tC3fcS7LbHJuGg' 
