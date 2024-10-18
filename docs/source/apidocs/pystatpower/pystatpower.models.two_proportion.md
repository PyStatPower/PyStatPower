# {py:mod}`pystatpower.models.two_proportion`

```{py:module} pystatpower.models.two_proportion
```

```{autodoc2-docstring} pystatpower.models.two_proportion
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Target <pystatpower.models.two_proportion.Target>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.Target
    :summary:
    ```
* - {py:obj}`TestType <pystatpower.models.two_proportion.TestType>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.TestType
    :summary:
    ```
* - {py:obj}`GroupAllocationOption <pystatpower.models.two_proportion.GroupAllocationOption>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption
    :summary:
    ```
* - {py:obj}`GroupAllocation <pystatpower.models.two_proportion.GroupAllocation>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocation
    :summary:
    ```
* - {py:obj}`GroupAllocationForSize <pystatpower.models.two_proportion.GroupAllocationForSize>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForSize
    :summary:
    ```
* - {py:obj}`GroupAllocationForNotSize <pystatpower.models.two_proportion.GroupAllocationForNotSize>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForNotSize
    :summary:
    ```
* - {py:obj}`GroupAllocationForAlpha <pystatpower.models.two_proportion.GroupAllocationForAlpha>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForAlpha
    :summary:
    ```
* - {py:obj}`GroupAllocationForPower <pystatpower.models.two_proportion.GroupAllocationForPower>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForPower
    :summary:
    ```
* - {py:obj}`GroupAllocationForTreatmentProportion <pystatpower.models.two_proportion.GroupAllocationForTreatmentProportion>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForTreatmentProportion
    :summary:
    ```
* - {py:obj}`GroupAllocationForReferenceProportion <pystatpower.models.two_proportion.GroupAllocationForReferenceProportion>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForReferenceProportion
    :summary:
    ```
* - {py:obj}`TwoProportion <pystatpower.models.two_proportion.TwoProportion>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fun_power <pystatpower.models.two_proportion.fun_power>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.fun_power
    :summary:
    ```
* - {py:obj}`solve_for_sample_size <pystatpower.models.two_proportion.solve_for_sample_size>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_sample_size
    :summary:
    ```
* - {py:obj}`solve_for_alpha <pystatpower.models.two_proportion.solve_for_alpha>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_alpha
    :summary:
    ```
* - {py:obj}`solve_for_power <pystatpower.models.two_proportion.solve_for_power>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_power
    :summary:
    ```
* - {py:obj}`solve_for_treatment_proportion <pystatpower.models.two_proportion.solve_for_treatment_proportion>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_treatment_proportion
    :summary:
    ```
* - {py:obj}`solve_for_reference_proportion <pystatpower.models.two_proportion.solve_for_reference_proportion>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_reference_proportion
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <pystatpower.models.two_proportion.__all__>`
  - ```{autodoc2-docstring} pystatpower.models.two_proportion.__all__
    :summary:
    ```
````

### API

````{py:data} __all__
:canonical: pystatpower.models.two_proportion.__all__
:value: >
   ['GroupAllocation', 'solve_for_sample_size', 'solve_for_alpha', 'solve_for_power', 'solve_for_treatm...

```{autodoc2-docstring} pystatpower.models.two_proportion.__all__
```

````

`````{py:class} Target(*args, **kwds)
:canonical: pystatpower.models.two_proportion.Target

Bases: {py:obj}`enum.Enum`

```{autodoc2-docstring} pystatpower.models.two_proportion.Target
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.Target.__init__
```

````{py:attribute} SIZE
:canonical: pystatpower.models.two_proportion.Target.SIZE
:value: >
   1

```{autodoc2-docstring} pystatpower.models.two_proportion.Target.SIZE
```

````

````{py:attribute} ALPHA
:canonical: pystatpower.models.two_proportion.Target.ALPHA
:value: >
   2

```{autodoc2-docstring} pystatpower.models.two_proportion.Target.ALPHA
```

````

````{py:attribute} POWER
:canonical: pystatpower.models.two_proportion.Target.POWER
:value: >
   3

```{autodoc2-docstring} pystatpower.models.two_proportion.Target.POWER
```

````

````{py:attribute} TREATMENT_PROPORTION
:canonical: pystatpower.models.two_proportion.Target.TREATMENT_PROPORTION
:value: >
   4

```{autodoc2-docstring} pystatpower.models.two_proportion.Target.TREATMENT_PROPORTION
```

````

````{py:attribute} REFERENCE_PROPORTION
:canonical: pystatpower.models.two_proportion.Target.REFERENCE_PROPORTION
:value: >
   5

```{autodoc2-docstring} pystatpower.models.two_proportion.Target.REFERENCE_PROPORTION
```

````

`````

`````{py:class} TestType(*args, **kwds)
:canonical: pystatpower.models.two_proportion.TestType

Bases: {py:obj}`enum.Enum`

```{autodoc2-docstring} pystatpower.models.two_proportion.TestType
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.TestType.__init__
```

````{py:attribute} Z_TEST_POOLED
:canonical: pystatpower.models.two_proportion.TestType.Z_TEST_POOLED
:value: >
   1

```{autodoc2-docstring} pystatpower.models.two_proportion.TestType.Z_TEST_POOLED
```

````

````{py:attribute} Z_TEST_UNPOOLED
:canonical: pystatpower.models.two_proportion.TestType.Z_TEST_UNPOOLED
:value: >
   2

```{autodoc2-docstring} pystatpower.models.two_proportion.TestType.Z_TEST_UNPOOLED
```

````

````{py:attribute} Z_TEST_CC_POOLED
:canonical: pystatpower.models.two_proportion.TestType.Z_TEST_CC_POOLED
:value: >
   3

```{autodoc2-docstring} pystatpower.models.two_proportion.TestType.Z_TEST_CC_POOLED
```

````

````{py:attribute} Z_TEST_CC_UNPOOLED
:canonical: pystatpower.models.two_proportion.TestType.Z_TEST_CC_UNPOOLED
:value: >
   4

```{autodoc2-docstring} pystatpower.models.two_proportion.TestType.Z_TEST_CC_UNPOOLED
```

````

`````

`````{py:class} GroupAllocationOption(*args, **kwds)
:canonical: pystatpower.models.two_proportion.GroupAllocationOption

Bases: {py:obj}`enum.Flag`

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.__init__
```

````{py:attribute} EQUAL
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.EQUAL
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.EQUAL
```

````

````{py:attribute} SIZE_OF_TOTAL
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.SIZE_OF_TOTAL
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.SIZE_OF_TOTAL
```

````

````{py:attribute} SIZE_OF_EACH
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.SIZE_OF_EACH
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.SIZE_OF_EACH
```

````

````{py:attribute} SIZE_OF_TREATMENT
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.SIZE_OF_TREATMENT
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.SIZE_OF_TREATMENT
```

````

````{py:attribute} SIZE_OF_REFERENCE
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.SIZE_OF_REFERENCE
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.SIZE_OF_REFERENCE
```

````

````{py:attribute} RATIO_OF_TREATMENT_TO_REFERENCE
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.RATIO_OF_TREATMENT_TO_REFERENCE
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.RATIO_OF_TREATMENT_TO_REFERENCE
```

````

````{py:attribute} RATIO_OF_REFERENCE_TO_TREATMENT
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.RATIO_OF_REFERENCE_TO_TREATMENT
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.RATIO_OF_REFERENCE_TO_TREATMENT
```

````

````{py:attribute} PERCENT_OF_TREATMENT
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.PERCENT_OF_TREATMENT
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.PERCENT_OF_TREATMENT
```

````

````{py:attribute} PERCENT_OF_REFERENCE
:canonical: pystatpower.models.two_proportion.GroupAllocationOption.PERCENT_OF_REFERENCE
:value: >
   'auto(...)'

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationOption.PERCENT_OF_REFERENCE
```

````

`````

`````{py:class} GroupAllocation(size_of_total: float = None, size_of_each: float = None, size_of_treatment: float = None, size_of_reference: float = None, ratio_of_treatment_to_reference: float = None, ratio_of_reference_to_treatment: float = None, percent_of_treatment: float = None, percent_of_reference: float = None)
:canonical: pystatpower.models.two_proportion.GroupAllocation

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocation
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocation.__init__
```

````{py:method} get_group_allocation_for_target(target: pystatpower.models.two_proportion.Target)
:canonical: pystatpower.models.two_proportion.GroupAllocation.get_group_allocation_for_target

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocation.get_group_allocation_for_target
```

````

`````

````{py:class} GroupAllocationForSize(size_of_treatment: float = None, size_of_reference: float = None, ratio_of_treatment_to_reference: float = None, ratio_of_reference_to_treatment: float = None, percent_of_treatment: float = None, percent_of_reference: float = None)
:canonical: pystatpower.models.two_proportion.GroupAllocationForSize

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForSize
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForSize.__init__
```

````

````{py:class} GroupAllocationForNotSize(size_of_total: float = None, size_of_each: float = None, size_of_treatment: float = None, size_of_reference: float = None, ratio_of_treatment_to_reference: float = None, ratio_of_reference_to_treatment: float = None, percent_of_treatment: float = None, percent_of_reference: float = None)
:canonical: pystatpower.models.two_proportion.GroupAllocationForNotSize

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForNotSize
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForNotSize.__init__
```

````

````{py:class} GroupAllocationForAlpha(size_of_total: float = None, size_of_each: float = None, size_of_treatment: float = None, size_of_reference: float = None, ratio_of_treatment_to_reference: float = None, ratio_of_reference_to_treatment: float = None, percent_of_treatment: float = None, percent_of_reference: float = None)
:canonical: pystatpower.models.two_proportion.GroupAllocationForAlpha

Bases: {py:obj}`pystatpower.models.two_proportion.GroupAllocationForNotSize`

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForAlpha
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForAlpha.__init__
```

````

````{py:class} GroupAllocationForPower(size_of_total: float = None, size_of_each: float = None, size_of_treatment: float = None, size_of_reference: float = None, ratio_of_treatment_to_reference: float = None, ratio_of_reference_to_treatment: float = None, percent_of_treatment: float = None, percent_of_reference: float = None)
:canonical: pystatpower.models.two_proportion.GroupAllocationForPower

Bases: {py:obj}`pystatpower.models.two_proportion.GroupAllocationForNotSize`

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForPower
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForPower.__init__
```

````

````{py:class} GroupAllocationForTreatmentProportion(size_of_total: float = None, size_of_each: float = None, size_of_treatment: float = None, size_of_reference: float = None, ratio_of_treatment_to_reference: float = None, ratio_of_reference_to_treatment: float = None, percent_of_treatment: float = None, percent_of_reference: float = None)
:canonical: pystatpower.models.two_proportion.GroupAllocationForTreatmentProportion

Bases: {py:obj}`pystatpower.models.two_proportion.GroupAllocationForNotSize`

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForTreatmentProportion
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForTreatmentProportion.__init__
```

````

````{py:class} GroupAllocationForReferenceProportion(size_of_total: float = None, size_of_each: float = None, size_of_treatment: float = None, size_of_reference: float = None, ratio_of_treatment_to_reference: float = None, ratio_of_reference_to_treatment: float = None, percent_of_treatment: float = None, percent_of_reference: float = None)
:canonical: pystatpower.models.two_proportion.GroupAllocationForReferenceProportion

Bases: {py:obj}`pystatpower.models.two_proportion.GroupAllocationForNotSize`

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForReferenceProportion
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.GroupAllocationForReferenceProportion.__init__
```

````

````{py:function} fun_power(alpha: float, treatment_n: float, reference_n: float, treatment_proportion: float, reference_proportion: float, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.two_proportion.TestType)
:canonical: pystatpower.models.two_proportion.fun_power

```{autodoc2-docstring} pystatpower.models.two_proportion.fun_power
```
````

``````{py:class} TwoProportion
:canonical: pystatpower.models.two_proportion.TwoProportion

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion
```

`````{py:class} ForSize(alpha: pystatpower.numeric.Alpha, power: pystatpower.numeric.Power, treatment_proportion: pystatpower.numeric.Proportion, reference_proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.two_proportion.TestType, group_allocation: pystatpower.models.two_proportion.GroupAllocationForSize, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.two_proportion.TwoProportion.ForSize

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForSize
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForSize.__init__
```

````{py:method} solve()
:canonical: pystatpower.models.two_proportion.TwoProportion.ForSize.solve

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForSize.solve
```

````

`````

`````{py:class} ForAlpha(power: pystatpower.numeric.Power, treatment_proportion: pystatpower.numeric.Proportion, reference_proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.two_proportion.TestType, group_allocation: pystatpower.models.two_proportion.GroupAllocationForAlpha, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.two_proportion.TwoProportion.ForAlpha

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForAlpha
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForAlpha.__init__
```

````{py:method} solve()
:canonical: pystatpower.models.two_proportion.TwoProportion.ForAlpha.solve

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForAlpha.solve
```

````

`````

`````{py:class} ForPower(alpha: pystatpower.numeric.Alpha, treatment_proportion: pystatpower.numeric.Proportion, reference_proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.two_proportion.TestType, group_allocation: pystatpower.models.two_proportion.GroupAllocationForPower, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.two_proportion.TwoProportion.ForPower

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForPower
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForPower.__init__
```

````{py:method} solve()
:canonical: pystatpower.models.two_proportion.TwoProportion.ForPower.solve

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForPower.solve
```

````

`````

`````{py:class} ForTreatmentProportion(alpha: pystatpower.numeric.Alpha, power: pystatpower.numeric.Power, reference_proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.two_proportion.TestType, group_allocation: pystatpower.models.two_proportion.GroupAllocationForTreatmentProportion, search_direction: pystatpower.option.SearchDirection, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.two_proportion.TwoProportion.ForTreatmentProportion

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForTreatmentProportion
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForTreatmentProportion.__init__
```

````{py:method} solve()
:canonical: pystatpower.models.two_proportion.TwoProportion.ForTreatmentProportion.solve

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForTreatmentProportion.solve
```

````

`````

`````{py:class} ForReferenceProportion(alpha: pystatpower.numeric.Alpha, power: pystatpower.numeric.Power, treatment_proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.two_proportion.TestType, group_allocation: pystatpower.models.two_proportion.GroupAllocationForReferenceProportion, search_direction: pystatpower.option.SearchDirection, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.two_proportion.TwoProportion.ForReferenceProportion

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForReferenceProportion
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForReferenceProportion.__init__
```

````{py:method} solve()
:canonical: pystatpower.models.two_proportion.TwoProportion.ForReferenceProportion.solve

```{autodoc2-docstring} pystatpower.models.two_proportion.TwoProportion.ForReferenceProportion.solve
```

````

`````

``````

````{py:function} solve_for_sample_size(alpha: float, power: float, treatment_proportion: float, reference_proportion: float, alternative: str, test_type: str, group_allocation: pystatpower.models.two_proportion.GroupAllocation = GroupAllocation(), dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.two_proportion.solve_for_sample_size

```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_sample_size
```
````

````{py:function} solve_for_alpha(power: float, treatment_proportion: float, reference_proportion: float, alternative: str, test_type: str, group_allocation: pystatpower.models.two_proportion.GroupAllocation, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.two_proportion.solve_for_alpha

```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_alpha
```
````

````{py:function} solve_for_power(alpha: float, treatment_proportion: float, reference_proportion: float, alternative: str, test_type: str, group_allocation: pystatpower.models.two_proportion.GroupAllocation, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.two_proportion.solve_for_power

```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_power
```
````

````{py:function} solve_for_treatment_proportion(alpha: float, power: float, reference_proportion: float, alternative: str, test_type: str, group_allocation: pystatpower.models.two_proportion.GroupAllocation, search_direction: pystatpower.option.SearchDirection, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.two_proportion.solve_for_treatment_proportion

```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_treatment_proportion
```
````

````{py:function} solve_for_reference_proportion(alpha: float, power: float, treatment_proportion: float, alternative: str, test_type: str, group_allocation: pystatpower.models.two_proportion.GroupAllocation, search_direction: str, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.two_proportion.solve_for_reference_proportion

```{autodoc2-docstring} pystatpower.models.two_proportion.solve_for_reference_proportion
```
````
