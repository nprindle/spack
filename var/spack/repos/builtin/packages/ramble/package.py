# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ramble(SConsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/asrivast28/ramBLe"

    git = "https://github.com/asrivast28/ramBLe"
    version('master', submodules=True)

    variant('test', default=False)
    variant('logging', default=False)
    variant('timer', default=False)

    # FIXME: Add dependencies if required.
    depends_on('boost+mpi@1.70:')
    depends_on('mpi')
    depends_on('googletest', when='+test')

    def build_args(self, spec, prefix):
        args = []
        args.append('TEST={}'.format('1' if '+test' in spec else '0'))
        args.append('LOGGING={}'.format('1' if '+logging' in spec else '0'))
        args.append('TIMER={}'.format('1' if '+timer' in spec else '0'))
        return args

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('ramble', prefix.bin)
