#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):


        # EVEX.128.66.0F38.W0 a2 /vsib
        # vscatterdps vm32x {k1}, xmm1

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.aaa = 1
        Buffer = '{}a2443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Options = ShowEVEXMasking
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xa2)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vscatterdps ')
        assert_equal(myDisasm.instr.repr, 'vscatterdps dword ptr [rbx+xmm6+0088h] {k1}, xmm0')

        # EVEX.256.66.0F38.W0 a2 /vsib
        # vscatterdps vm32y {k1}, ymm1

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.aaa = 1
        Buffer = '{}a2443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Options = ShowEVEXMasking
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xa2)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vscatterdps ')
        assert_equal(myDisasm.instr.repr, 'vscatterdps dword ptr [rbx+ymm6+0088h] {k1}, ymm0')

        # EVEX.512.66.0F38.W0 a2 /vsib
        # vscatterdps vm32z {k1}, zmm1

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.aaa = 1
        Buffer = '{}a2443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Options = ShowEVEXMasking
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xa2)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vscatterdps ')
        assert_equal(myDisasm.instr.repr, 'vscatterdps dword ptr [rbx+zmm6+0088h] {k1}, zmm0')

        # EVEX.128.66.0F38.W1 a2 /vsib
        # vscatterdpd vm32x {k1}, xmm1

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        myEVEX.aaa = 1
        Buffer = '{}a2443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Options = ShowEVEXMasking
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xa2)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vscatterdpd ')
        assert_equal(myDisasm.instr.repr, 'vscatterdpd dword ptr [rbx+xmm6+0110h] {k1}, xmm0')

        # EVEX.256.66.0F38.W1 a2 /vsib
        # vscatterdpd vm32x {k1}, ymm1

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        myEVEX.aaa = 1
        Buffer = '{}a2443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Options = ShowEVEXMasking
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xa2)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vscatterdpd ')
        assert_equal(myDisasm.instr.repr, 'vscatterdpd dword ptr [rbx+xmm6+0110h] {k1}, ymm0')

        # EVEX.512.66.0F38.W1 a2 /vsib
        # vscatterdpd vm32y {k1}, zmm1

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        myEVEX.aaa = 1
        Buffer = '{}a2443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Options = ShowEVEXMasking
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xa2)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vscatterdpd ')
        assert_equal(myDisasm.instr.repr, 'vscatterdpd dword ptr [rbx+ymm6+0110h] {k1}, zmm0')