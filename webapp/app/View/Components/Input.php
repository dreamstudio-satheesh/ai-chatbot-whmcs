<?php

namespace App\View\Components;

class Input extends FormControl
{
    public $checked;

    public function __construct($name, $id = null, $value = '', $label = '', $bag = 'default', $type = 'text')
    {
        parent::__construct($name, $id, $value, $label, $bag);
        $this->formControlAttributes = $this->formControlAttributes->merge(['type' => $type]);
    }

    public function render()
    {
        return view('components.input');
    }
}
