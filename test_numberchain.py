#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from numberchain import numberchain, reference_implementation, correct_solution


def test_numberchain():
    assert_equals(numberchain(1), 1)

def test_numberchain_two_numbers():
    assert_equals(numberchain(2,1), 21)

def test_numberchain_three_numbers():
    assert_equals(numberchain(1,1,1), 111)
    
def test_numberchain_4():
    assert_equals(numberchain(1,2,3,4), 4321)

def test_numberchain_5():
    assert_equals(numberchain(10,2), 210)
    
def test_numberchain_6():
    assert_equals(numberchain(20, 1), 201)
    
def test_numberchain_7():
    assert_equals(numberchain(50, 2, 1, 9), 95021)
    
def test_numberchain_8():
    assert_equals(numberchain(420, 42, 423), 42423420)
    
def test_numberchain_9():
    assert_equals(numberchain(420, 42, 423, 4), 442423420)
    
def test_numberchain_10():
    assert_equals(numberchain(420, 423, 4), 4423420)
    
def test_numberchain_11():
    assert_equals(numberchain(420, 423, 4, 45), 454423420)
    
def test_numberchain_12():
    assert_equals(numberchain(420, 423, 4, 450), 4504423420)
    
def test_numberchain_13():
    assert_equals(numberchain(420, 423, 4, 41), 442342041)

def test_numberchain_14():
    assert_equals(numberchain(4209, 4239, 4, 414), 442394209414)

def test_numberchain_15():
    assert_equals(numberchain(420, 424, 4, 45), 454424420)
    
def test_numberchain_16():
    numbers = (42424242421, 423, 425, 42)
    assert_equals(numberchain(*numbers), correct_solution(*numbers))
    
def test_numberchain_17():
    assert_equals(numberchain(42424242425, 423, 425, 42), 4254242424242542423)
    
def test_numberchain_18():
    numbers = (4242424241, 423, 425, 42)
    assert_equals(numberchain(*numbers), correct_solution(*numbers))
    
def test_numberchain_19():
    assert_equals(numberchain(4242424247, 423, 425, 42), 425424242424742423)
    

def test_numberchain_really_correct_1():
    numbers = (4242424247, 423, 425, 42)
    assert_equals(numberchain(*numbers), correct_solution(*numbers))
    
def test_numberchain_really_correct_2():
    numbers = (42423, 42425, 42)
    assert_equals(numberchain(*numbers), correct_solution(*numbers))
    
def test_numberchain_really_correct_3():
    numbers = (4242423, 4242425, 42)
    assert_equals(numberchain(*numbers), correct_solution(*numbers))
    
def test_numberchain_with_reference_1():
    numbers = (4242423, 4242425, 42)
    assert_equals(reference_implementation(*numbers), correct_solution(*numbers))
