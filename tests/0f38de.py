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
    """
    Variable Blend Packed
    """

    def test(self):

        # F3 0F 38 DE !(11):rrr:bbb
        # AESENC256KL xmm, m512

        Buffer = bytes.fromhex('f30f38de00')
        myDisasm = Disasm(Buffer)
        length = myDisasm.read()
        assert_equal(length, len(Buffer))
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf38de)
        assert_equal(myDisasm.infos.Instruction.Category, KL_INSTRUCTION)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'aesenc256kl ')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE)
        assert_equal(myDisasm.infos.Operand1.Registers.xmm, REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 512)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.repr(), 'aesenc256kl xmm0,  [rax]')

        # 66 0F 38 DC /r
        # AESdec xmm1, xmm2/m128

        Buffer = bytes.fromhex('660f38de6bA2')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf38de')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'aesdec ')
        assert_equal(myDisasm.repr(), 'aesdec xmm5, xmmword ptr [rbx-5Eh]')


        # VEX.NDS.128.66.0F38.WIG DC /r
        # VAESdec xmm1, xmm2, xmm3/m128

        myVEX = VEX()
        myVEX.L = 0
        myVEX.pp = 0b1
        myVEX.mmmm = 0b10
        myVEX.vvvv = 0b1111
        myVEX.R = 1
        myVEX.B = 1

        Buffer = bytes.fromhex('c4{:02x}{:02x}de6ba2'.format(myVEX.byte1(), myVEX.byte2()))
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.repr(), 'vaesdec xmm5, xmm0, xmmword ptr [rbx-5Eh]')

        # if VEX.vvvv != 0b1111 #UD

        myVEX.reset()
        myVEX.L = 0
        myVEX.pp = 0b1
        myVEX.mmmm = 0b10
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.B = 1

        Buffer = bytes.fromhex('c4{:02x}{:02x}de6ba2'.format(myVEX.byte1(), myVEX.byte2()))
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'vaesdec ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)
