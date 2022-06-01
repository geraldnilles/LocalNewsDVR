# THis test script seems to work well streaming and trasncoding video into H264 and AAC on the RPI

library="/tmp/localnews"
mkdir -p $library
cd $library

ffmpeg \
    -y \
    -i http://10.0.0.240:5004/auto/v2.1 \
    -num_capture_buffers 64 \
    -c:v h264_v4l2m2m \
    -b:v 5M \
    -c:a aac \
    -ac 2 \
    out.mp4

