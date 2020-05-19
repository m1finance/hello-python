#!/bin/bash
set -eu
export AWS_ACCESS_KEY_ID=$ACCESS_KEY_ID_ENV_VAR_NAME
export AWS_SECRET_ACCESS_KEY=$SECRET_ACCESS_KEY_ENV_VAR_NAME

eval $(aws ecr get-login --region us-east-1 --no-include-email)
CUR_CHART_VERSION=$(cat chart/Chart.yaml | grep "version:" | awk -F ': ' '{ print $2 }')
CHART_VERSION="$VERSION+$CIRCLE_SHA1"
sed -i .bak 's/'$CUR_CHART_VERSION'/'$CHART_VERSION'/g' chart/Chart.yaml
tar -czvf ./chart.tgz ./chart
aws s3 cp ./chart.tgz s3://m1-develop-chart-museum/hello-python/${DOCKER_TAG}-chart.tgz