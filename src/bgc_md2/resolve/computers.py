from sympy import Symbol, ImmutableMatrix
from functools import lru_cache
import numpy as np
from typing import Tuple
from sympy.physics.units import Quantity
from .mvars import (
    InFluxesBySymbol,
    OutFluxesBySymbol,
    InternalFluxesBySymbol,
    CarbonInFluxesBySymbol,
    CarbonOutFluxesBySymbol,
    CarbonInternalFluxesBySymbol,
    NitrogenInFluxesBySymbol,
    NitrogenOutFluxesBySymbol,
    NitrogenInternalFluxesBySymbol,
    TimeSymbol,
    StateVariableTuple,
    CarbonStateVariableTuple,
    NitrogenStateVariableTuple,
    CompartmentalMatrix,
    CarbonCompartmentalMatrix,
    NitrogenCompartmentalMatrix,
    # CompartmentalMatrixStructure,
    InputTuple,
    CarbonInputTuple,
    NitrogenInputTuple,
    VegetationCarbonInputScalar,
    VegetationCarbonInputPartitioningTuple,
    VegetationCarbonInputTuple,
    VegetationCarbonStateVariableTuple,
    VegetationCarbonCompartmentalMatrix,
    VegetationCarbonInFluxesBySymbol,
    VegetationCarbonOutFluxesBySymbol,
    VegetationCarbonInternalFluxesBySymbol,
    NumericSimulationTimes,
    NumericParameterization,
    NumericStartValueArray,
    NumericStartValueDict,
    NumericParameterizedSmoothReservoirModel,
    NumericSolutionArray,
    QuantityParameterization,
    QuantitySimulationTimes,
    QuantityParameterizedSmoothReservoirModel,
    QuantityStartValueDict,
    QuantityStartValueArray,
    QuantityModelRun,
    QuantitySolutionArray,
    StateVarUnitTuple,
)
from CompartmentalSystems.smooth_reservoir_model import SmoothReservoirModel
import CompartmentalSystems.helpers_reservoir as hr
from CompartmentalSystems.smooth_model_run import SmoothModelRun

@lru_cache
def vegetation_carbon_in_fluxes_by_symbol_1(
    in_fluxes: InFluxesBySymbol,
    out_fluxes: OutFluxesBySymbol,
    internal_fluxes: InternalFluxesBySymbol,
    svt: StateVariableTuple,
    vcsvt: VegetationCarbonStateVariableTuple
) -> VegetationCarbonInFluxesBySymbol:
    svt_set=frozenset({v for v in svt})
    vcsvt_set=frozenset({v for v in vcsvt})
    combined = (
        svt_set,
        in_fluxes,
        out_fluxes,
        internal_fluxes,
    )

    _,in_fluxes_veg,out_fluxes_veg,internal_fluxes_veg=hr.extract(combined,vcsvt_set)
    
    return VegetationCarbonInFluxesBySymbol( in_fluxes_veg)

@lru_cache
def vegetation_carbon_out_fluxes_by_symbol_1(
    in_fluxes: InFluxesBySymbol,
    out_fluxes: OutFluxesBySymbol,
    internal_fluxes: InternalFluxesBySymbol,
    svt: StateVariableTuple,
    vcsvt: VegetationCarbonStateVariableTuple
) -> VegetationCarbonOutFluxesBySymbol:
    svt_set=frozenset({v for v in svt})
    vcsvt_set=frozenset({v for v in vcsvt})
    combined = (
        svt_set,
        in_fluxes,
        out_fluxes,
        internal_fluxes,
    )

    _,in_fluxes_veg,out_fluxes_veg,internal_fluxes_veg=hr.extract(combined,vcsvt_set)
    
    return VegetationCarbonOutFluxesBySymbol( out_fluxes_veg)

@lru_cache
def vegetation_carbon_internal_fluxes_by_symbol_1(
    in_fluxes: InFluxesBySymbol,
    out_fluxes: OutFluxesBySymbol,
    internal_fluxes: InternalFluxesBySymbol,
    svt: StateVariableTuple,
    vcsvt: VegetationCarbonStateVariableTuple
) -> VegetationCarbonInternalFluxesBySymbol:
    svt_set=frozenset({v for v in svt})
    vcsvt_set=frozenset({v for v in vcsvt})
    combined = (
        svt_set,
        in_fluxes,
        out_fluxes,
        internal_fluxes,
    )

    _,in_fluxes_veg,out_fluxes_veg,internal_fluxes_veg=hr.extract(combined,vcsvt_set)
    
    return VegetationCarbonInternalFluxesBySymbol( internal_fluxes_veg)

@lru_cache
def vegetation_carbon_compartmental_matrix_1(
    in_fluxes: InFluxesBySymbol,
    out_fluxes: OutFluxesBySymbol,
    internal_fluxes: InternalFluxesBySymbol,
    svt: StateVariableTuple,
    vcsvt: VegetationCarbonStateVariableTuple
) -> VegetationCarbonCompartmentalMatrix:
    svt_set=frozenset({v for v in svt})
    vcsvt_set=frozenset({v for v in vcsvt})
    combined = (
        svt_set,
        in_fluxes,
        out_fluxes,
        internal_fluxes,
    )

    _,in_fluxes_veg,out_fluxes_veg,internal_fluxes_veg=hr.extract(combined,vcsvt_set)
    cm=hr.compartmental_matrix_2(
        out_fluxes_veg,
        internal_fluxes_veg,
        vcsvt
    )
    return VegetationCarbonCompartmentalMatrix(cm)

@lru_cache
def smooth_reservoir_model_from_fluxes(
    in_fluxes: InFluxesBySymbol,
    out_fluxes: OutFluxesBySymbol,
    internal_fluxes: InternalFluxesBySymbol,
    time_symbol: TimeSymbol,
    state_variable_tuple: StateVariableTuple,
) -> SmoothReservoirModel:
    return SmoothReservoirModel.from_state_variable_indexed_fluxes(
        state_vector=list(state_variable_tuple),
        time_symbol=time_symbol,
        input_fluxes=in_fluxes,
        output_fluxes=out_fluxes,
        internal_fluxes=internal_fluxes,
    )

@lru_cache
def smooth_reservoir_model_from_input_tuple_and_matrix(
    u: InputTuple,
    B: CompartmentalMatrix,
    time_symbol: TimeSymbol,
    state_variable_tuple: StateVariableTuple,
) -> SmoothReservoirModel:
    return SmoothReservoirModel.from_B_u(
        state_vector=ImmutableMatrix(state_variable_tuple),
        time_symbol=time_symbol,
        B=B,
        u=ImmutableMatrix(u),
    )


@lru_cache
def in_fluxes_by_symbol_1(
    u: InputTuple,
    svt: StateVariableTuple
) -> InFluxesBySymbol:
    return InFluxesBySymbol(hr.in_fluxes_by_symbol(svt,u))


@lru_cache
def internal_fluxes_by_symbol_1(
    cm: CompartmentalMatrix,
    svt: StateVariableTuple
) -> InternalFluxesBySymbol:
    return InternalFluxesBySymbol(hr.internal_fluxes_by_symbol(svt,cm))


@lru_cache
def out_fluxes_by_symbol_1(
    cm: CompartmentalMatrix,
    svt: StateVariableTuple
) -> OutFluxesBySymbol:
    return OutFluxesBySymbol(hr.out_fluxes_by_symbol(svt,cm))


@lru_cache
def carbon_in_fluxes_by_symbol_1(
    u: CarbonInputTuple,
    svt: CarbonStateVariableTuple
) -> CarbonInFluxesBySymbol:
    return CarbonInFluxesBySymbol(hr.in_fluxes_by_symbol(svt,u))


@lru_cache
def carbon_internal_fluxes_by_symbol_1(
    cm: CarbonCompartmentalMatrix,
    svt: CarbonStateVariableTuple
) -> CarbonInternalFluxesBySymbol:
    return CarbonInternalFluxesBySymbol(hr.internal_fluxes_by_symbol(svt,cm))


@lru_cache
def nitrogen_out_fluxes_by_symbol_1(
    cm: NitrogenCompartmentalMatrix,
    svt: NitrogenStateVariableTuple
) -> NitrogenOutFluxesBySymbol:
    return NitrogenOutFluxesBySymbol(hr.out_fluxes_by_symbol(svt,cm))

@lru_cache
def nitrogen_in_fluxes_by_symbol_1(
    u: NitrogenInputTuple,
    svt: NitrogenStateVariableTuple
) -> NitrogenInFluxesBySymbol:
    return NitrogenInFluxesBySymbol(hr.in_fluxes_by_symbol(svt,u))

@lru_cache
def nitrogen_in_fluxes_by_symbol_2(
    fl: InFluxesBySymbol,
    svt: NitrogenStateVariableTuple
) -> NitrogenInFluxesBySymbol:
    return NitrogenInFluxesBySymbol(
        {v: f for v, f in fl.items() if v in svt}
    )

@lru_cache
def nitrogen_out_fluxes_by_symbol_2(
    fl: OutFluxesBySymbol,
    svt: NitrogenStateVariableTuple
) -> NitrogenOutFluxesBySymbol:
    return NitrogenOutFluxesBySymbol(
        {v: f for v, f in fl.items() if v in svt}
    )

@lru_cache
def nitrogen_internal_fluxes_by_symbol_2(
    fl: InternalFluxesBySymbol,
    svt: NitrogenStateVariableTuple
) -> NitrogenInternalFluxesBySymbol:
    return NitrogenInternalFluxesBySymbol(
        {t: f for t, f in fl.items() if set(t).issubset(svt)}
    )

@lru_cache
def carbon_in_fluxes_by_symbol_2(
    fl: InFluxesBySymbol,
    svt: CarbonStateVariableTuple
) -> CarbonInFluxesBySymbol:
    return CarbonInFluxesBySymbol(
        {v: f for v, f in fl.items() if v in svt}
    )

@lru_cache
def carbon_out_fluxes_by_symbol_2(
    fl: OutFluxesBySymbol,
    svt: CarbonStateVariableTuple
) -> CarbonOutFluxesBySymbol:
    return CarbonOutFluxesBySymbol(
        {v: f for v, f in fl.items() if v in svt}
    )

@lru_cache
def carbon_internal_fluxes_by_symbol_2(
    fl: InternalFluxesBySymbol,
    svt: CarbonStateVariableTuple
) -> CarbonInternalFluxesBySymbol:
    return CarbonInternalFluxesBySymbol(
        {t: f for t, f in fl.items() if set(t).issubset(svt)}
    )

@lru_cache
def nitrogen_internal_fluxes_by_symbol_1(
    cm: NitrogenCompartmentalMatrix,
    svt: NitrogenStateVariableTuple
) -> NitrogenInternalFluxesBySymbol:
    return NitrogenInternalFluxesBySymbol(hr.internal_fluxes_by_symbol(svt,cm))

@lru_cache
def carbon_out_fluxes_by_symbol_1(
    cm: CarbonCompartmentalMatrix,
    svt: CarbonStateVariableTuple
) -> CarbonOutFluxesBySymbol:
    return CarbonOutFluxesBySymbol(hr.out_fluxes_by_symbol(svt,cm))

@lru_cache
def compartmental_matrix_from_smooth_reservoir_model(
    smr: SmoothReservoirModel,
) -> CompartmentalMatrix:
    return CompartmentalMatrix(smr.compartmental_matrix)

@lru_cache
def compartmental_matrix_2(
    ofl: OutFluxesBySymbol,
    ifl: InternalFluxesBySymbol,
    svt: StateVariableTuple
) -> CompartmentalMatrix:
    return CompartmentalMatrix(
        hr.compartmental_matrix_2(
            ofl,
            ifl,
            svt
        )
    )

@lru_cache
def nitrogen_compartmental_matrix_2(
    ofl: NitrogenOutFluxesBySymbol,
    ifl: NitrogenInternalFluxesBySymbol,
    svt: NitrogenStateVariableTuple
) -> NitrogenCompartmentalMatrix:
    return NitrogenCompartmentalMatrix(
        hr.compartmental_matrix_2(
            ofl,
            ifl,
            svt
        )
    )

@lru_cache
def vegetation_carbon_input_tuple_1(
    u: VegetationCarbonInputScalar, b: VegetationCarbonInputPartitioningTuple
) -> VegetationCarbonInputTuple:
    return VegetationCarbonInputTuple(b * u)


@lru_cache
def vegetation_carbon_input_tuple_2(
    ifls: VegetationCarbonInFluxesBySymbol,
    vcsv: VegetationCarbonStateVariableTuple

) -> VegetationCarbonInputTuple:
    return VegetationCarbonInputTuple(hr.in_or_out_flux_tuple(vcsv, ifls))


@lru_cache
def vegetation_carbon_input_scalar_1(
    t: VegetationCarbonInputTuple
) -> VegetationCarbonInputScalar:
    return VegetationCarbonInputScalar(sum(t))


@lru_cache
def vegetation_carbon_input_partitioning_tuple_1(
    u: VegetationCarbonInputScalar,
    t: VegetationCarbonInputTuple
) -> VegetationCarbonInputPartitioningTuple:
    return VegetationCarbonInputPartitioningTuple(
        [tc/u for tc in t]
    )


# @lru_cache
def numeric_model_run_1(
    npsrm: NumericParameterizedSmoothReservoirModel,
    start_values_num: NumericStartValueArray,
    times_num: NumericSimulationTimes,
) -> SmoothModelRun:
    return SmoothModelRun(
        npsrm.srm,
        npsrm.parameterization.par_dict,
        start_values_num,
        times_num,
        npsrm.parameterization.func_dict,
    )


@lru_cache
def numeric_parameterized_smooth_reservoir_model_1(
    srm: SmoothReservoirModel, para_num: NumericParameterization,
) -> NumericParameterizedSmoothReservoirModel:
    return NumericParameterizedSmoothReservoirModel(srm, para_num)


@lru_cache
def numeric_start_value_array_1(
    nsvd: NumericStartValueDict,
    svt: StateVariableTuple
) -> NumericStartValueArray:
    tup = tuple(nsvd[k] for k in svt)
    return NumericStartValueArray(tup)


@lru_cache
def numeric_start_value_array_2(
    smr: SmoothModelRun
) -> NumericStartValueArray:
    return NumericStartValueArray(smr.start_values)


@lru_cache
def numeric_start_value_dict(
    nsva: NumericStartValueArray,
    svt: StateVariableTuple
) -> NumericStartValueDict:
    return NumericStartValueDict({sv:nsva[i]  for i,sv in enumerate(svt)})


@lru_cache
def numeric_solution_array_1(
    smr: SmoothModelRun
) -> NumericSolutionArray:
    return NumericSolutionArray(smr.solve())


@lru_cache
def quantity_parameterization_1(
    npar: NumericParameterization,
    state_var_units: StateVarUnitTuple,
    time_unit: Quantity
) -> QuantityParameterization:
    return QuantityParameterization(
        npar.par_dict,
        npar.func_dict,
        state_var_units,
        time_unit
    )


@lru_cache
def quantity_parameterized_smooth_reservoir_model_1(
    srm: SmoothReservoirModel,
    para_q: QuantityParameterization
) -> QuantityParameterizedSmoothReservoirModel:
    return QuantityParameterizedSmoothReservoirModel(srm, para_q)


@lru_cache
def quantity_start_value_array_1(
    qsvd: QuantityStartValueDict,
    svt: StateVariableTuple
) -> QuantityStartValueArray:
    tup = tuple(qsvd[k] for k in svt)
    return QuantityStartValueArray(tup)


# @lru_cache
def quantity_model_run_1(
    qpsrm: QuantityParameterizedSmoothReservoirModel,
    start_values_q: QuantityStartValueArray,
    times_q: QuantitySimulationTimes,
) -> QuantityModelRun:
    return QuantityModelRun(
        qpsrm,
        start_values_q,
        times_q,
    )


@lru_cache
def quantity_solution_array_1(
    qmr: QuantityModelRun
) -> QuantitySolutionArray:
    return QuantitySolutionArray(qmr.solve())


@lru_cache
def smooth_reservoir_model_2(
    smr: SmoothModelRun
) -> SmoothReservoirModel:
    return smr.model

