<?php

namespace App\View\Components;

class Radio extends FormControl
{
    public $checked;

    public function __construct($name, $id = null, $value = '', $label = '', $bag = 'default')
    {
        parent::__construct($name, $id, $value, $label, $bag);
        $this->value = $value;
    }

    public function render()
    {
        return view('components.radio');
    }
}
