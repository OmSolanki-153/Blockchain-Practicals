// Aim: Write a Solidity program that demonstrates various types of functions including regular functions, view functions, pure functions, and the fallback function. 
// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.0; 
contract FunctionTypesDemo { 
 
    uint public counter = 0; 
 
    //     Regular function: modifies the state 
    function increment() public { 
        counter += 1; 
    } 
 
    //          View function: reads state, doesn't modify 
    function getCounter() public view returns (uint) { 
        return counter; 
    } 
 
    //        Pure function: no access to state 
    function add(uint a, uint b) public pure returns (uint) { 
        return a + b; 
    } 
 
    //    Receive function: triggered when contract receives Ether with no data 
    receive() external payable { 
        // You could add logic here for receiving ETH 
    } 
 
    //      Fallback function: triggered when no other function matches 
    fallback() external payable { 
        // Fallback logic can go here 
    } 
    
