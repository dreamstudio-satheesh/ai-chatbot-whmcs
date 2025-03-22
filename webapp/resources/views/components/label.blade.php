@props(['value'])

<label {{ $attributes->class(['block text-sm font-medium leading-tight text-gray-800 dark:text-white']) }}>{{ $value ?? $slot }}</label>
