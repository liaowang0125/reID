#!/usr/bin/env sh
MY=/home/lw/dgd_person_reid_old

echo 'Create gallery lmdb..'
rm -rf $MY/external/exp/db/img/P2_gallery_lmdb
/home/lw/caffe/build/tools/convert_imageset \
--resize_height=160 \
--resize_width=64 \
$MY/reiddata2/P2/ \
$MY/reiddata2/P2/P2_gallery.txt \
$MY/external/exp/db/img/P2_gallery_lmdb

echo "Create probe lmdb.."
rm -rf $MY/external/exp/db/img/P2_probe_lmdb
/home/lw/caffe/build/tools/convert_imageset \
--resize_height=160 \
--resize_width=64 \
$MY/reiddata2/P2/ \
$MY/reiddata2/P2/P2_probe.txt \
$MY/external/exp/db/img/P2_probe_lmdb


echo "All Done.."