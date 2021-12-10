import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings

def test_default():

    Model.clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings(1, 'Geometrisch-linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    Model.clientModel.service.finish_modification()

def test_GeometricallyLinear():

    Model.clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings.GeometricallyLinear(1,2,'Geometric-linear',[True, 1.5, True],False,False,StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,[True,0,0,1.0])

    Model.clientModel.service.finish_modification()

def test_LargeDeformation():

    Model.clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings.LargeDeformation(1,standard_precision_and_tolerance_settings = [True, 0.01, 0.01, 1.0],)

    Model.clientModel.service.finish_modification()

def test_SecondOrderPDelta():

    Model.clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings.SecondOrderPDelta(1)

    Model.clientModel.service.finish_modification()

