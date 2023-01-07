import Editor from "@monaco-editor/react";


const defaultOptions = {
    selectOnLineNumbers: true,
    roundedSelection: false,
    readOnly: false,
    cursorStyle: 'line',
    theme: 'vs-dark',
    minimap: {
        enabled: false
    },
    // scrollbar: {
    //     // Subtle shadows to the left & top. Defaults to true.
    //     useShadows: false,
    //     // Render vertical arrows. Defaults to false.
    //     verticalHasArrows: true,
    //     // Render horizontal arrows. Defaults to false.
    //     horizontalHasArrows: true,
    //     // Render vertical scrollbar.
    //     // Accepted values: 'auto', 'visible', 'hidden'.
    //     // Defaults to 'auto'
    //     vertical: 'visible',
    //     // Render horizontal scrollbar.
    //     // Accepted values: 'auto', 'visible', 'hidden'.
    //     // Defaults to 'auto'
    //     horizontal: 'visible',
    //     verticalScrollbarSize: 17,
    //     horizontalScrollbarSize: 17,
    //     arrowSize: 30,
    // }
};


const readOnlyOptions = {
    selectOnLineNumbers: true,
    roundedSelection: false,
    readOnly: true,
    cursorStyle: 'line',
    theme: 'vs-dark',
    minimap: {
        enabled: false
    }
}

export const Console = ({ children, readOnly, code = '', setCode }) => {
    let options = readOnly ? readOnlyOptions : defaultOptions;
    console.log(options)
    return (
        <div className='col d-flex flex-column justify-content-evenly'>
            <Editor
                theme="vs-dark"
                defaultLanguage="rust"
                value={code}
                onChange={setCode}
                options = {options}
            />

            {children}
        </div>
    )
}


