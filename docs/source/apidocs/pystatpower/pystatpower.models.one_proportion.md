# {py:mod}`pystatpower.models.one_proportion`

```{py:module} pystatpower.models.one_proportion
```

```{autodoc2-docstring} pystatpower.models.one_proportion
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestType <pystatpower.models.one_proportion.TestType>`
  - ```{autodoc2-docstring} pystatpower.models.one_proportion.TestType
    :summary:
    ```
* - {py:obj}`OneProportion <pystatpower.models.one_proportion.OneProportion>`
  - ```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fun_power <pystatpower.models.one_proportion.fun_power>`
  - ```{autodoc2-docstring} pystatpower.models.one_proportion.fun_power
    :summary:
    ```
* - {py:obj}`solve_for_sample_size <pystatpower.models.one_proportion.solve_for_sample_size>`
  - ```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_sample_size
    :summary:
    ```
* - {py:obj}`solve_for_alpha <pystatpower.models.one_proportion.solve_for_alpha>`
  - ```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_alpha
    :summary:
    ```
* - {py:obj}`solve_for_power <pystatpower.models.one_proportion.solve_for_power>`
  - ```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_power
    :summary:
    ```
* - {py:obj}`solve_for_nullproportion <pystatpower.models.one_proportion.solve_for_nullproportion>`
  - ```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_nullproportion
    :summary:
    ```
* - {py:obj}`solve_for_proportion <pystatpower.models.one_proportion.solve_for_proportion>`
  - ```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_proportion
    :summary:
    ```
````

### API

`````{py:class} TestType(*args, **kwds)
:canonical: pystatpower.models.one_proportion.TestType

Bases: {py:obj}`enum.Enum`

```{autodoc2-docstring} pystatpower.models.one_proportion.TestType
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.one_proportion.TestType.__init__
```

````{py:attribute} EXACT_TEST
:canonical: pystatpower.models.one_proportion.TestType.EXACT_TEST
:value: >
   'Exact Test'

```{autodoc2-docstring} pystatpower.models.one_proportion.TestType.EXACT_TEST
```

````

````{py:attribute} Z_TEST_USING_S_P0
:canonical: pystatpower.models.one_proportion.TestType.Z_TEST_USING_S_P0
:value: >
   'Z-Test using S(P0)'

```{autodoc2-docstring} pystatpower.models.one_proportion.TestType.Z_TEST_USING_S_P0
```

````

````{py:attribute} Z_TEST_USING_S_P0_CC
:canonical: pystatpower.models.one_proportion.TestType.Z_TEST_USING_S_P0_CC
:value: >
   'Z-Test using S(P0) with Continuity Correction'

```{autodoc2-docstring} pystatpower.models.one_proportion.TestType.Z_TEST_USING_S_P0_CC
```

````

````{py:attribute} Z_TEST_USING_S_PHAT
:canonical: pystatpower.models.one_proportion.TestType.Z_TEST_USING_S_PHAT
:value: >
   'Z-Test using S(PHat)'

```{autodoc2-docstring} pystatpower.models.one_proportion.TestType.Z_TEST_USING_S_PHAT
```

````

````{py:attribute} Z_TEST_USING_S_PHAT_CC
:canonical: pystatpower.models.one_proportion.TestType.Z_TEST_USING_S_PHAT_CC
:value: >
   'Z-Test using S(PHat) with Continuity Correction'

```{autodoc2-docstring} pystatpower.models.one_proportion.TestType.Z_TEST_USING_S_PHAT_CC
```

````

`````

````{py:function} fun_power(size: float, alpha: float, nullproportion: float, proportion: float, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.one_proportion.TestType) -> float
:canonical: pystatpower.models.one_proportion.fun_power

```{autodoc2-docstring} pystatpower.models.one_proportion.fun_power
```
````

``````{py:class} OneProportion
:canonical: pystatpower.models.one_proportion.OneProportion

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion
```

`````{py:class} ForSize(alpha: pystatpower.numeric.Alpha, power: pystatpower.numeric.Power, nullproportion: pystatpower.numeric.Proportion, proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.one_proportion.TestType, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.one_proportion.OneProportion.ForSize

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForSize
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForSize.__init__
```

````{py:method} solve() -> pystatpower.numeric.Size
:canonical: pystatpower.models.one_proportion.OneProportion.ForSize.solve

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForSize.solve
```

````

`````

`````{py:class} ForAlpha(size: pystatpower.numeric.Size, power: pystatpower.numeric.Power, nullproportion: pystatpower.numeric.Proportion, proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.one_proportion.TestType, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.one_proportion.OneProportion.ForAlpha

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForAlpha
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForAlpha.__init__
```

````{py:method} solve() -> pystatpower.numeric.Alpha
:canonical: pystatpower.models.one_proportion.OneProportion.ForAlpha.solve

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForAlpha.solve
```

````

`````

`````{py:class} ForPower(size: pystatpower.numeric.Size, alpha: pystatpower.numeric.Alpha, nullproportion: pystatpower.numeric.Proportion, proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.one_proportion.TestType, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.one_proportion.OneProportion.ForPower

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForPower
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForPower.__init__
```

````{py:method} solve() -> pystatpower.numeric.Power
:canonical: pystatpower.models.one_proportion.OneProportion.ForPower.solve

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForPower.solve
```

````

`````

`````{py:class} ForNullProportion(size: pystatpower.numeric.Size, alpha: pystatpower.numeric.Alpha, power: pystatpower.numeric.Power, proportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.one_proportion.TestType, search_direction: pystatpower.option.SearchDirection, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.one_proportion.OneProportion.ForNullProportion

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForNullProportion
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForNullProportion.__init__
```

````{py:method} solve() -> pystatpower.numeric.Proportion
:canonical: pystatpower.models.one_proportion.OneProportion.ForNullProportion.solve

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForNullProportion.solve
```

````

`````

`````{py:class} ForProportion(size: pystatpower.numeric.Size, alpha: pystatpower.numeric.Alpha, power: pystatpower.numeric.Power, nullproportion: pystatpower.numeric.Proportion, alternative: pystatpower.option.Alternative, test_type: pystatpower.models.one_proportion.TestType, search_direction: pystatpower.option.SearchDirection, dropout_rate: pystatpower.numeric.DropOutRate)
:canonical: pystatpower.models.one_proportion.OneProportion.ForProportion

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForProportion
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForProportion.__init__
```

````{py:method} solve() -> pystatpower.numeric.Proportion
:canonical: pystatpower.models.one_proportion.OneProportion.ForProportion.solve

```{autodoc2-docstring} pystatpower.models.one_proportion.OneProportion.ForProportion.solve
```

````

`````

``````

````{py:function} solve_for_sample_size(alpha: float, power: float, nullproportion: float, proportion: float, alternative: str, test_type: str, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.one_proportion.solve_for_sample_size

```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_sample_size
```
````

````{py:function} solve_for_alpha(size: float, power: float, nullproportion: float, proportion: float, alternative: str, test_type: str, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.one_proportion.solve_for_alpha

```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_alpha
```
````

````{py:function} solve_for_power(size: float, alpha: float, nullproportion: float, proportion: float, alternative: str, test_type: str, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.one_proportion.solve_for_power

```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_power
```
````

````{py:function} solve_for_nullproportion(size: float, alpha: float, power: float, proportion: float, alternative: str, test_type: str, search_direction: str, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.one_proportion.solve_for_nullproportion

```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_nullproportion
```
````

````{py:function} solve_for_proportion(size: float, alpha: float, power: float, nullproportion: float, alternative: str, test_type: str, search_direction: str, dropout_rate: float = 0, full_output: bool = False)
:canonical: pystatpower.models.one_proportion.solve_for_proportion

```{autodoc2-docstring} pystatpower.models.one_proportion.solve_for_proportion
```
````
