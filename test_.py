import pytest
import hashlib
import json
import numpy as np
from testbook import testbook

@pytest.fixture(scope='module')
def tb():
  with testbook('hw1.ipynb', execute=True) as tb:
    yield tb

    
def test_step_1(tb):
  
  try:
    complete = None
    complete = tb.ref('STEP_1_COMPLETE')
  except:
    # STEP_1_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 1: not complete.'
   
    
def test_step_2(tb):
  try:
    complete = None
    complete = tb.ref('STEP_2_COMPLETE')
  except:
    # STEP_2_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 2: not complete.'
    
    
def test_step_3(tb):
  try:
    complete = None
    complete = tb.ref('STEP_3_COMPLETE')
  except:
    # STEP_3_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 3: not complete.'

    
def test_step_4(tb):
  try:
    complete = None
    complete = tb.ref('STEP_4_COMPLETE')
  except:
    # STEP_4_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 4: not complete.'   
    
    
def test_step_5(tb):
  try:
    complete = None
    complete = tb.ref('STEP_5_COMPLETE')
  except:
    # STEP_5_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 5: not complete.'  
    
    
def test_step_6(tb):
  try:
    complete = None
    complete = tb.ref('STEP_6_COMPLETE')
  except:
    # STEP_6_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 6: not complete.' 
    
    
def test_step_7(tb):
  try:
    complete = None
    complete = tb.ref('STEP_7_COMPLETE')
  except:
    # STEP_7_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 7: not complete.'    
    
    
def test_step_8(tb):
  try:
    complete = None
    complete = tb.ref('STEP_8_COMPLETE')
  except:
    # STEP_8_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 8: not complete.'    
    
    
def test_step_9(tb):
  try:
    complete = None
    complete = tb.ref('STEP_9_COMPLETE')
  except:
    # STEP_9_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 9: not complete.'    
    
    
def test_step_10(tb):
  try:
    complete = None
    complete = tb.ref('STEP_10_COMPLETE')
  except:
    # STEP_10_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 10: not complete.'    
    
    
def test_step_11(tb):
  try:
    complete = None
    complete = tb.ref('STEP_11_COMPLETE')
  except:
    # STEP_11_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 11: not complete.'    
    
    
def test_step_12(tb):
  try:
    complete = None
    complete = tb.ref('STEP_12_COMPLETE')
  except:
    # STEP_12_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 12: not complete.'    
    
    
def test_step_13(tb):
  try:
    complete = None
    complete = tb.ref('STEP_13_COMPLETE')
  except:
    # STEP_13_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 13: not complete.'    
    
  tb.execute_cell('step13')
  beta0 = tb.ref('beta0')
  beta1 = exec('np.' + tb.ref('beta1').resolve())
  assert np.isclose(beta0, 39.93586102117047), 'STEP 13: The value for beta0 is incorrect'
  print(tb.ref('beta1').resolve())
  print(beta1)
  print(tb.ref('r2'))
  print(tb.ref('mse'))
  
#     39.93586102117047
#   'array([-0.15784473])'
#   0.6059482578894348
#   23.943662938603108
  assert False
    
def test_step_14(tb):
  try:
    complete = None
    complete = tb.ref('STEP_14_COMPLETE')
  except:
    # STEP_14_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 14: not complete.'    
    
    
def test_step_15(tb):
  try:
    complete = None
    complete = tb.ref('STEP_15_COMPLETE')
  except:
    # STEP_15_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 15: not complete.' 
