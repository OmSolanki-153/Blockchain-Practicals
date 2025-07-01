// Aim: Write a Solidity program that demonstrates function overloading, mathematical functions, and cryptographic functions. 
 
// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.0; 
 
contract PracticalDemo { 
 
    //      Function Overloading Example 
    function getResult(uint a, uint b, uint c) public pure returns (uint) { 
        return a + b + c; 
    } 
 
    //        Mathematical Functions 
    function mathOps(uint a, uint b) public pure returns ( 
        uint sum, 
        uint diff, 
        uint prod, 
        uint quotient, 
        uint mod, 
        uint power 
    ) { 
        require(b != 0, "Division by zero"); // avoids divide-by-zero error 
        sum = a + b; 
        diff = a - b; 
        prod = a * b; 
        quotient = a / b; 
        mod = a % b; 
        power = a ** b; 
    } 
 
    //      Cryptographic Hash Functions 
 
    function hashKeccak256(string memory input) public pure returns (bytes32) { 
        return keccak256(abi.encodePacked(input)); 
    } 
 
    function hashSha256(string memory input) public pure returns (bytes32) { 
        return sha256(abi.encodePacked(input)); 
    } 
 
    function hashRipemd160(string memory input) public pure returns (bytes20) { 
        return ripemd160(abi.encodePacked(input)); 
}
}
