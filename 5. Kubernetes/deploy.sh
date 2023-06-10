#!/bin/bash
kubectl apply -f k8s/init/
sleep 2
kubectl apply -f k8s/service/


# wait for mysql is ready
STR=$(kubectl get pod | grep mysql)
SUB='Running'
if [[ "$STR" == *"$SUB"* ]]; then
  running=1
else
  running=0
fi

while [ $running = 0 ]
do
  STR=$(kubectl get pod | grep mysql)
  if [[ "$STR" == *"$SUB"* ]]; then
    running=1
  else
    running=0
  fi
  sleep 1
done

sleep 1
chmod -R 777 db/
