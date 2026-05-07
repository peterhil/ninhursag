<script lang="ts">
	import type { PageData } from './$types'
	import type { MineralsOutput } from '$lib/types'

	import Minerals from '$component/Minerals.svelte'
	import { mineral } from '$store/mineral'

	type OutputProps = PageData & MineralsOutput

	interface Props {
		data: OutputProps
	}

	let { data }: Props = $props()
</script>

<svelte:head>
	<title>{data.mineral} statistics | Ninhursag</title>
</svelte:head>

<div class="page">
	<Minerals {data}/>
</div>
