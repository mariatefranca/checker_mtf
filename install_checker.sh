#!/bin/bash
crontab -l >.checker_cron
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo "0 23 * * * ${SCRIPT_DIR}/sitechecker.sh >>${SCRIPT_DIR}/cron_resultado.txt" >>.checker_cron
crontab .checker_cron
rm .checker_cron
echo Checker adicionado ao cron, certifique-se que o cron está rodando:
echo   sudo service cron start
