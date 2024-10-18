# {py:mod}`pystatpower.exception`

```{py:module} pystatpower.exception
```

```{autodoc2-docstring} pystatpower.exception
:allowtitles:
```

## Module Contents

### API

`````{py:exception} EnumMemberNotExistError(enum: enum.Enum, value: str)
:canonical: pystatpower.exception.EnumMemberNotExistError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} pystatpower.exception.EnumMemberNotExistError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.EnumMemberNotExistError.__init__
```

````{py:method} __repr__() -> str
:canonical: pystatpower.exception.EnumMemberNotExistError.__repr__

````

````{py:method} __str__() -> str
:canonical: pystatpower.exception.EnumMemberNotExistError.__str__

````

`````

`````{py:exception} ParameterError(message: str)
:canonical: pystatpower.exception.ParameterError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} pystatpower.exception.ParameterError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.ParameterError.__init__
```

````{py:method} __repr__() -> str
:canonical: pystatpower.exception.ParameterError.__repr__

````

````{py:method} __str__() -> str
:canonical: pystatpower.exception.ParameterError.__str__

````

`````

````{py:exception} ParameterTypeError(message: str)
:canonical: pystatpower.exception.ParameterTypeError

Bases: {py:obj}`pystatpower.exception.ParameterError`

```{autodoc2-docstring} pystatpower.exception.ParameterTypeError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.ParameterTypeError.__init__
```

````

````{py:exception} ParameterValueNotInDomainError(message: str)
:canonical: pystatpower.exception.ParameterValueNotInDomainError

Bases: {py:obj}`pystatpower.exception.ParameterError`

```{autodoc2-docstring} pystatpower.exception.ParameterValueNotInDomainError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.ParameterValueNotInDomainError.__init__
```

````

````{py:exception} ParameterValueEmptyError(message: str)
:canonical: pystatpower.exception.ParameterValueEmptyError

Bases: {py:obj}`pystatpower.exception.ParameterError`

```{autodoc2-docstring} pystatpower.exception.ParameterValueEmptyError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.ParameterValueEmptyError.__init__
```

````

````{py:exception} TargetParameterError(message: str)
:canonical: pystatpower.exception.TargetParameterError

Bases: {py:obj}`pystatpower.exception.ParameterError`

```{autodoc2-docstring} pystatpower.exception.TargetParameterError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.TargetParameterError.__init__
```

````

````{py:exception} TargetParameterNotExistError(message: str)
:canonical: pystatpower.exception.TargetParameterNotExistError

Bases: {py:obj}`pystatpower.exception.TargetParameterError`

```{autodoc2-docstring} pystatpower.exception.TargetParameterNotExistError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.TargetParameterNotExistError.__init__
```

````

````{py:exception} TargetParameterNotUniqueError(message: str)
:canonical: pystatpower.exception.TargetParameterNotUniqueError

Bases: {py:obj}`pystatpower.exception.TargetParameterError`

```{autodoc2-docstring} pystatpower.exception.TargetParameterNotUniqueError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.TargetParameterNotUniqueError.__init__
```

````

`````{py:exception} CalculationError(message: str)
:canonical: pystatpower.exception.CalculationError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} pystatpower.exception.CalculationError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.CalculationError.__init__
```

````{py:method} __repr__() -> str
:canonical: pystatpower.exception.CalculationError.__repr__

````

````{py:method} __str__() -> str
:canonical: pystatpower.exception.CalculationError.__str__

````

`````

````{py:exception} CalculationSolutionNotFoundError(message: str)
:canonical: pystatpower.exception.CalculationSolutionNotFoundError

Bases: {py:obj}`pystatpower.exception.CalculationError`

```{autodoc2-docstring} pystatpower.exception.CalculationSolutionNotFoundError
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.exception.CalculationSolutionNotFoundError.__init__
```

````
