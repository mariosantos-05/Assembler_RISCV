# RISC-V RV32I Assembler

A Python-based assembler for the RISC-V RV32I instruction set. This project parses `.asm` source files and generates hexadecimal machine code output in MIF (Memory Initialization File) format, supporting basic integer instructions and memory operations.

## Features
- Parses RISC-V RV32I assembly instructions
- Supports `.text` and `.data` sections
- Generates `.mif` output files
- Handles registers, immediates, and basic branching

## Motivation
This project was developed as part of Lab 01 for the Computer Organization and Architecture course *CIC0099*. The goal is to better understand low-level programming, instruction encoding, and how assembly code is translated into machine code within a RISC-V architecture.

## Usage
```bash
[placeholder]
```

## Supported Instructions
- add, sub, and, or, xor
- addi, andi, ori, xori
- lw, sw
- beq, bne
- jal, jalr
- lui, auipc
