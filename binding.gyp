{
  'variables': {
    'WEBRTC_ROOT%': '/root/webrtc/src',
    'FLAVOR%': 'Debug'
  },
  'targets': [
    {
      'target_name': 'webrtcjs',
      'sources': [
        'src/recording_decoder.cc',
        'src/observers.cc',
        'src/peerconnection.cc',
        'src/eventemitter.cc',
        'src/webrtcjs.cc'
      ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        '<@(WEBRTC_ROOT)/chromium/src/third_party/jsoncpp/source/include',
        '<@(WEBRTC_ROOT)>',
      ],
      'cflags': [
        '-fPIC'
      ],
      'defines': [
        'WEBRTC_POSIX',
        'BUILDING_NODE_EXTENSION',
        '_LARGEFILE_SOURCE',
        '_FILE_OFFSET_BITS=64',
        '_GLIBCXX_DEBUG=0',
      ],
      'link_settings': {
        'libraries': [
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/talk/libjingle_peerconnection.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/p2p/librtc_p2p.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/base/librtc_base.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/talk/libjingle_p2p.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/media/librtc_media.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/jsoncpp/libjsoncpp.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/boringssl/libboringssl.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/boringssl/libboringssl_asm.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libvideo_render_module.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libcng.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/openmax_dl/dl/libopenmax_dl.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/librent_a_codec.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/voice_engine/libvoice_engine.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libaudio_coding_module.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libneteq.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libg711.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libpcm16b.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libilbc.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libwebrtc_opus.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/opus/libopus.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libg722.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libisac.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libisac_common.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libred.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libaudio_encoder_interface.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libaudio_decoder_interface.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libmedia_file.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/libyuv.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libjpeg_turbo/libjpeg_turbo.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/libwebrtc.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/libwebrtc_common.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/librtc_event_log.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/librtc_event_log_proto.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libwebrtc_utility.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libaudio_conference_mixer.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libaudio_processing.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/common_audio/libcommon_audio.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/common_audio/libcommon_audio_sse2.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libaudioproc_debug_proto.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/protobuf/libprotobuf_lite.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libaudio_processing_sse2.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libaudio_device.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libbitrate_controller.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libpaced_sender.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/librtp_rtcp.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libremote_bitrate_estimator.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libvideo_capture_module.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libvideo_processing.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libvideo_processing_sse2.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libwebrtc_video_coding.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libwebrtc_h264.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libwebrtc_i420.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/video_coding/codecs/vp8/libwebrtc_vp8.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/common_video/libcommon_video.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/video_coding/utility/libvideo_coding_utility.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libvpx_new/libvpx_new.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libvpx_new/libvpx_intrinsics_mmx.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libvpx_new/libvpx_intrinsics_sse2.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libvpx_new/libvpx_intrinsics_ssse3.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libvpx_new/libvpx_intrinsics_sse4_1.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libvpx_new/libvpx_intrinsics_avx.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libvpx_new/libvpx_intrinsics_avx2.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/video_coding/codecs/vp9/libwebrtc_vp9.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/sound/librtc_sound.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/system_wrappers/libmetrics_default.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/libjingle/xmllite/librtc_xmllite.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/libjingle/xmpp/librtc_xmpp.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libvideo_capture_module_internal_impl.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/modules/libvideo_render_module_internal_impl.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/usrsctp/libusrsctplib.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/chromium/src/third_party/libsrtp/libsrtp.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/system_wrappers/libfield_trial_default.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/system_wrappers/libsystem_wrappers.a',
          '<@(WEBRTC_ROOT)/out/<@(FLAVOR)/obj/webrtc/base/librtc_base_approved.a',
          '-lX11',
        ],
      }
    }
  ]
}
