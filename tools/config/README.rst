=======================================
Auto-generation of sample configuration
=======================================

This generate_sample.sh tool is used to generate etc/solum/solum_guestagent.conf.sample

Run it from the top-level working directory i.e.

  $> ./tools/config/generate_sample.sh -b ./ -p solum_guestagent -o etc/solum

Watch out for warnings about modules like libvirt, qpid and zmq not
being found - these warnings are significant because they result
in options not appearing in the generated config file.
