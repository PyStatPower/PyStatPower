# {py:mod}`pystatpower.numeric`

```{py:module} pystatpower.numeric
```

```{autodoc2-docstring} pystatpower.numeric
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Interval <pystatpower.numeric.Interval>`
  - ```{autodoc2-docstring} pystatpower.numeric.Interval
    :summary:
    ```
* - {py:obj}`PowerAnalysisFloat <pystatpower.numeric.PowerAnalysisFloat>`
  - ```{autodoc2-docstring} pystatpower.numeric.PowerAnalysisFloat
    :summary:
    ```
* - {py:obj}`Alpha <pystatpower.numeric.Alpha>`
  - ```{autodoc2-docstring} pystatpower.numeric.Alpha
    :summary:
    ```
* - {py:obj}`Power <pystatpower.numeric.Power>`
  - ```{autodoc2-docstring} pystatpower.numeric.Power
    :summary:
    ```
* - {py:obj}`Mean <pystatpower.numeric.Mean>`
  - ```{autodoc2-docstring} pystatpower.numeric.Mean
    :summary:
    ```
* - {py:obj}`STD <pystatpower.numeric.STD>`
  - ```{autodoc2-docstring} pystatpower.numeric.STD
    :summary:
    ```
* - {py:obj}`Proportion <pystatpower.numeric.Proportion>`
  - ```{autodoc2-docstring} pystatpower.numeric.Proportion
    :summary:
    ```
* - {py:obj}`Percent <pystatpower.numeric.Percent>`
  - ```{autodoc2-docstring} pystatpower.numeric.Percent
    :summary:
    ```
* - {py:obj}`Ratio <pystatpower.numeric.Ratio>`
  - ```{autodoc2-docstring} pystatpower.numeric.Ratio
    :summary:
    ```
* - {py:obj}`Size <pystatpower.numeric.Size>`
  - ```{autodoc2-docstring} pystatpower.numeric.Size
    :summary:
    ```
* - {py:obj}`DropOutRate <pystatpower.numeric.DropOutRate>`
  - ```{autodoc2-docstring} pystatpower.numeric.DropOutRate
    :summary:
    ```
* - {py:obj}`DropOutSize <pystatpower.numeric.DropOutSize>`
  - ```{autodoc2-docstring} pystatpower.numeric.DropOutSize
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MIN_FLOAT <pystatpower.numeric.MIN_FLOAT>`
  - ```{autodoc2-docstring} pystatpower.numeric.MIN_FLOAT
    :summary:
    ```
* - {py:obj}`MAX_FLOAT <pystatpower.numeric.MAX_FLOAT>`
  - ```{autodoc2-docstring} pystatpower.numeric.MAX_FLOAT
    :summary:
    ```
````

### API

````{py:data} MIN_FLOAT
:canonical: pystatpower.numeric.MIN_FLOAT
:type: float
:value: >
   1e-10

```{autodoc2-docstring} pystatpower.numeric.MIN_FLOAT
```

````

````{py:data} MAX_FLOAT
:canonical: pystatpower.numeric.MAX_FLOAT
:type: float
:value: >
   10000000000.0

```{autodoc2-docstring} pystatpower.numeric.MAX_FLOAT
```

````

`````{py:class} Interval
:canonical: pystatpower.numeric.Interval

```{autodoc2-docstring} pystatpower.numeric.Interval
```

````{py:attribute} lower
:canonical: pystatpower.numeric.Interval.lower
:type: int | float
:value: >
   None

```{autodoc2-docstring} pystatpower.numeric.Interval.lower
```

````

````{py:attribute} upper
:canonical: pystatpower.numeric.Interval.upper
:type: int | float
:value: >
   None

```{autodoc2-docstring} pystatpower.numeric.Interval.upper
```

````

````{py:attribute} lower_inclusive
:canonical: pystatpower.numeric.Interval.lower_inclusive
:type: bool
:value: >
   False

```{autodoc2-docstring} pystatpower.numeric.Interval.lower_inclusive
```

````

````{py:attribute} upper_inclusive
:canonical: pystatpower.numeric.Interval.upper_inclusive
:type: bool
:value: >
   False

```{autodoc2-docstring} pystatpower.numeric.Interval.upper_inclusive
```

````

````{py:method} __contains__(value: int | float) -> bool
:canonical: pystatpower.numeric.Interval.__contains__

```{autodoc2-docstring} pystatpower.numeric.Interval.__contains__
```

````

````{py:method} __eq__(other: object) -> bool
:canonical: pystatpower.numeric.Interval.__eq__

````

````{py:method} __repr__() -> str
:canonical: pystatpower.numeric.Interval.__repr__

````

````{py:method} pseudo_lbound(eps: float = MIN_FLOAT) -> float
:canonical: pystatpower.numeric.Interval.pseudo_lbound

```{autodoc2-docstring} pystatpower.numeric.Interval.pseudo_lbound
```

````

````{py:method} pseudo_ubound(eps: float = MIN_FLOAT) -> float
:canonical: pystatpower.numeric.Interval.pseudo_ubound

```{autodoc2-docstring} pystatpower.numeric.Interval.pseudo_ubound
```

````

````{py:method} pseudo_bound(eps: float = MIN_FLOAT) -> tuple[float, float]
:canonical: pystatpower.numeric.Interval.pseudo_bound

```{autodoc2-docstring} pystatpower.numeric.Interval.pseudo_bound
```

````

`````

`````{py:class} PowerAnalysisFloat()
:canonical: pystatpower.numeric.PowerAnalysisFloat

Bases: {py:obj}`float`

```{autodoc2-docstring} pystatpower.numeric.PowerAnalysisFloat
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.PowerAnalysisFloat.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.PowerAnalysisFloat.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.PowerAnalysisFloat.domain
```

````

````{py:method} __new__(obj)
:canonical: pystatpower.numeric.PowerAnalysisFloat.__new__

````

````{py:method} pseudo_bound() -> tuple[float, float]
:canonical: pystatpower.numeric.PowerAnalysisFloat.pseudo_bound
:classmethod:

```{autodoc2-docstring} pystatpower.numeric.PowerAnalysisFloat.pseudo_bound
```

````

`````

`````{py:class} Alpha()
:canonical: pystatpower.numeric.Alpha

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.Alpha
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.Alpha.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.Alpha.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.Alpha.domain
```

````

`````

`````{py:class} Power()
:canonical: pystatpower.numeric.Power

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.Power
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.Power.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.Power.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.Power.domain
```

````

`````

`````{py:class} Mean()
:canonical: pystatpower.numeric.Mean

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.Mean
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.Mean.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.Mean.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.Mean.domain
```

````

`````

`````{py:class} STD()
:canonical: pystatpower.numeric.STD

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.STD
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.STD.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.STD.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.STD.domain
```

````

`````

`````{py:class} Proportion()
:canonical: pystatpower.numeric.Proportion

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.Proportion
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.Proportion.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.Proportion.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.Proportion.domain
```

````

`````

`````{py:class} Percent()
:canonical: pystatpower.numeric.Percent

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.Percent
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.Percent.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.Percent.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.Percent.domain
```

````

`````

`````{py:class} Ratio()
:canonical: pystatpower.numeric.Ratio

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.Ratio
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.Ratio.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.Ratio.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.Ratio.domain
```

````

`````

`````{py:class} Size()
:canonical: pystatpower.numeric.Size

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.Size
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.Size.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.Size.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.Size.domain
```

````

`````

`````{py:class} DropOutRate()
:canonical: pystatpower.numeric.DropOutRate

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.DropOutRate
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.DropOutRate.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.DropOutRate.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.DropOutRate.domain
```

````

`````

`````{py:class} DropOutSize()
:canonical: pystatpower.numeric.DropOutSize

Bases: {py:obj}`pystatpower.numeric.PowerAnalysisFloat`

```{autodoc2-docstring} pystatpower.numeric.DropOutSize
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.numeric.DropOutSize.__init__
```

````{py:attribute} domain
:canonical: pystatpower.numeric.DropOutSize.domain
:value: >
   'Interval(...)'

```{autodoc2-docstring} pystatpower.numeric.DropOutSize.domain
```

````

`````
