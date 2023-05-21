import './style.scss'


export function Input({formik={}, name, ...rest}) {
    const {values, errors, touched, handleBlur, handleChange} = formik;
    return (
        <>
            <div className="bg-white border-bottom rounded px-2">
                <input
                    className="FormikInput Content_13 w-100 border-0 bg-transparent"
                    onChange={handleChange}
                    onBlur={handleBlur}
                    value={values?.[name]}
                    {...rest}
                />
            </div>
            <p className="text-danger Content_12">
                &nbsp;&nbsp;{touched?.[name] && errors?.[name] && errors?.[name]}
            </p>
        </>
    )
}


export function SelectInput({formik={}, name, options, ...rest}) {
    const {values, errors, touched, handleBlur, handleChange} = formik;
    const value = options?.findIndex(({value}) => value === values?.[name]) > -1
        ? values?.[name]
        : '' && (values[name] = '')
    return (
        <>
            <select className="SelectInput w-100 bg-white border rounded p-2"
                onChange={handleChange}
                onBlur={handleBlur}
                value={value}
                {...rest}
            >
                <option value='' label={`-- Select --`}/>
                {options?.map(({value, text}) => <option value={value} label={text} key={value}/>)}
            </select>
            <p className="text-danger Content_12">
                &nbsp;&nbsp;{touched?.[name] && errors?.[name] && errors?.[name]}
            </p>
        </>
    )
}

