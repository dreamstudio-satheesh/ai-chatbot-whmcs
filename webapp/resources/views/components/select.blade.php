@if(! $multiple)
  <select {{ $formControlAttributes }} {{ $attributes->merge(['class' => 'block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-blue-600 sm:text-sm sm:leading-6']) }}>
    @if($placeholder)
      <option value disabled {{ $isSelected('') ? 'selected' : '' }}>{{ $placeholder }}</option>
    @endif
    @if(! empty($options))
      @foreach($options as $v => $l)
        <option {{ $isSelected($v) ? 'selected' : '' }} value="{{ $v }}">{{ $l }}</option>
      @endforeach
    @else
      {{ $slot }}
    @endif
  </select>
@else
  <div {{ $attributes->merge(['class' => 'relative bg-gray-50 border overflow-x-hidden divide-y divide-gray-200 overflow-y-scroll h-40']) }}>
    @if(! empty($options))
      @foreach($options as $v => $l)
        <x-label for="{{ $name }}_{{ $loop->iteration }}" class="flex items-center space-x-2 w-full py-2 px-3 bg-white hover:bg-gray-50">
          <x-checkbox name="{{ $name }}" id="{{ $name }}_{{ $loop->iteration }}" value="{{ $v }}" :checked="$isSelected($v)" />
          <span>{{ $l }}</span>
        </x-label>
      @endforeach
    @else
      {{ $slot }}
    @endif
  </div>
@endif
