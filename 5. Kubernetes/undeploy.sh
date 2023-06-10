#!/bin/bash
kubectl delete -f k8s/service/
sleep 2
kubectl delete -f k8s/init/
rm -f db/binlog.*
