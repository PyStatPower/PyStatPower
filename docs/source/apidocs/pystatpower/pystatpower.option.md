# {py:mod}`pystatpower.option`

```{py:module} pystatpower.option
```

```{autodoc2-docstring} pystatpower.option
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Option <pystatpower.option.Option>`
  - ```{autodoc2-docstring} pystatpower.option.Option
    :summary:
    ```
* - {py:obj}`Alternative <pystatpower.option.Alternative>`
  - ```{autodoc2-docstring} pystatpower.option.Alternative
    :summary:
    ```
* - {py:obj}`SearchDirection <pystatpower.option.SearchDirection>`
  - ```{autodoc2-docstring} pystatpower.option.SearchDirection
    :summary:
    ```
````

### API

`````{py:class} Option
:canonical: pystatpower.option.Option

Bases: {py:obj}`enum.EnumMeta`

```{autodoc2-docstring} pystatpower.option.Option
```

````{py:method} __getitem__(name)
:canonical: pystatpower.option.Option.__getitem__

````

`````

`````{py:class} Alternative(*args, **kwds)
:canonical: pystatpower.option.Alternative

Bases: {py:obj}`enum.Enum`

```{autodoc2-docstring} pystatpower.option.Alternative
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.option.Alternative.__init__
```

````{py:attribute} TWO_SIDED
:canonical: pystatpower.option.Alternative.TWO_SIDED
:value: >
   1

```{autodoc2-docstring} pystatpower.option.Alternative.TWO_SIDED
```

````

````{py:attribute} ONE_SIDED
:canonical: pystatpower.option.Alternative.ONE_SIDED
:value: >
   2

```{autodoc2-docstring} pystatpower.option.Alternative.ONE_SIDED
```

````

`````

`````{py:class} SearchDirection(*args, **kwds)
:canonical: pystatpower.option.SearchDirection

Bases: {py:obj}`enum.Enum`

```{autodoc2-docstring} pystatpower.option.SearchDirection
```

```{rubric} Initialization
```

```{autodoc2-docstring} pystatpower.option.SearchDirection.__init__
```

````{py:attribute} LESS
:canonical: pystatpower.option.SearchDirection.LESS
:value: >
   1

```{autodoc2-docstring} pystatpower.option.SearchDirection.LESS
```

````

````{py:attribute} GREATER
:canonical: pystatpower.option.SearchDirection.GREATER
:value: >
   2

```{autodoc2-docstring} pystatpower.option.SearchDirection.GREATER
```

````

`````
