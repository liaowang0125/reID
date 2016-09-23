# Some constants
CAFFE_DIR=external/caffe

EXP_DIR=external/exp
DATASETS_DIR=${EXP_DIR}/datasets
DB_DIR=${EXP_DIR}/db
RESULTS_DIR=${EXP_DIR}/results
SNAPSHOTS_DIR=${EXP_DIR}/snapshots
NIS_DIR=${EXP_DIR}/nis

MODELS_DIR=models
LOGS_DIR=logs
get_trained_model() {
  local exp='individually'
  local dataset='viper'

  local solver=${MODELS_DIR}/${exp}/${dataset}_solver.prototxt
  local max_iter=$(grep 'max_iter' ${solver} | awk '{print dataset}')
  print local_max_iter