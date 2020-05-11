# Copyright (c) 2020, Huawei, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Willow Garage, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Author Zhen Ju/juzhen@huawei.com

from __future__ import print_function
import sys

from rospkg.os_detect import OS_OPENEULER, OS_RHEL

DEFAULT_RHEL_MAP_VER = '7.6'
OPENEULER_RHEL_VER_MAPS = {
    '20.03': '7.6'
}


def register_installers(context):
    pass


def register_platforms(context):
    register_openeuler(context)


def register_openeuler(context):
    # OpenEuler is derived from CentOS with a version mapping defined in OPENEULER_RHEL_VER_MAPS
    # Developer can set ROS_OS_OVERRIDE to 'centos:X.Y'
    (os_name, os_version) = context.get_os_name_and_version()
    compatible_centos_version = DEFAULT_RHEL_MAP_VER
    if os_version in OPENEULER_RHEL_VER_MAPS:
        compatible_centos_version = OPENEULER_RHEL_VER_MAPS[os_version]

    if os_name == OS_OPENEULER and not context.os_override:
        print('rosdep detected OS: [%s] aliasing it to: [%s]' %
              (OS_OPENEULER, OS_RHEL), file=sys.stderr)
        context.set_os_override(OS_RHEL, compatible_centos_version.split('.', 1)[0])
