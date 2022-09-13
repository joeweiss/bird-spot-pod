# bird-spot-pod

### MacOS M1

Bring it up and run:
`docker compose -f docker-compose.macm1.yml up -d --build`

To take it down:
`docker compose -f docker-compose.macm1.yml down`

To run bash within the docker instance:
`docker compose -f docker-compose.macm1.yml exec app bash`

To rebuild the image for a reason (e.g. after pip change)
`docker compose -f docker-compose.macm1.yml down; docker compose -f docker-compose.macm1.yml build --no-cache`
