---
layout: page
title: "Joint Learning of Wording and Formatting for Singable Melody-to-Lyric Generation"
permalink: /TC0WFOxq
---
 
<!-- Google Analytics tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MK1PD93QHP"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MK1PD93QHP');
</script>

# Journal of New Music Research 2023 Submission

Abstract: Despite previous efforts in melody-to-lyric generation research, there is still a significant singability gap between lyrics written by machines and human lyricists. This paper bridges the singability gap with a novel approach to generating singable lyrics by jointly Learning wOrding And Formatting during Melody-to-Lyric training (LOAF-M2L). After general-domain pretraining, our model acquires length awareness using unsupervised learning from a large text-only lyric corpus. Then, we introduce a new objective informed by musicological research on the relationship between melody and lyrics during melody-to-lyric supervised training, which enables the model to learn the fine-grained format requirements of the melody. Our model achieves 3.75% and 21.44% absolute accuracy gains in the outputs' number-of-line and syllable-per-line requirements compared to naive fine-tuning, without sacrificing text fluency. Furthermore, our model demonstrates a 42.15% and 74.18% relative improvement in overall quality in the subjective evaluation, compared to two leading melody-to-lyric generation models, highlighting the significance of formatting learning in lyric generation.

## Subjective Evaluation

### List of Songs

| Song No.  | #Paragraphs | Song Name |
| --------  | -------- | -------- |
| 1    | 2 | *Faded Love*, by by Bob Wills   |
| 2    | 2 | *Silent Lucidity*, by Queensrÿche   |
| 3    | 2 | *Free as Bird*, by The Beatles |
| 4    | 1 | *A Little Bit of Soap*, by The Jarmels |
| 5    | 2 | *Heart-Shaped Box*, by Nirvana |
| 6    | 2 | *People Got to be Free*, by The Rascals |

### List of Models

| Model  | Component |
| -------- | -------- |
| Original   | Original lyrics of the song   |
| AI-Lyricist   | The model from ([Ma et al. 2021](https://dl.acm.org/doi/abs/10.1145/3474085.3475502))   |
| SongMASS   | The model from ([Sheng et al. 2021](https://ojs.aaai.org/index.php/AAAI/article/view/17626)) |
| BART ft.  | Ablated model with only supervised fine-tuning |
| Unsupervised  | Ablated model with only unsupervised training |
| Ours   | Our model |

### Generation Results

<style>
.table-scroll {
  overflow-x: auto;
  width: 100%;
}
.table-scroll table {
  white-space: nowrap;
}
audio {
  width: 100px;      /* adjust to your taste */
  height: 30px;      /* Safari sometimes respects this */
}

audio.no-volume::-webkit-media-controls-volume-slider,
audio.no-volume::-webkit-media-controls-volume-control-container,
audio.no-volume::-webkit-media-controls-mute-button {
    display: none !important;
}
</style>


<!-- <div class="table-scroll" style="display: block; overflow-x: auto; width: 100%;" markdown="1">

| Model   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---------|---|---|---|---|---|---|---|---|---|----|
| Original | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 |
| Model 1  | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 |
| Model 2  | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 |
| Model 3  | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 |
| Model 4  | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 |
| Model 5  | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 |
| Model 6  | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 | pdf mp3 |

</div> -->

<div class="table-scroll" markdown="1">

| Paragraphs   | 1.1 | 1.2 | 2.1 | 2.2 | 3.1 | 3.2 | 4.1 | 5.1 | 5.2 | 6.1 | 6.2 |
|---------|---|---|---|---|---|---|---|---|---|----|----|
| Original | [sheet](/assets/for_projects/m2l/sheets/original/1_faded_love_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/1.1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/1_faded_love_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/1.2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/2_silent_lucidity_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/2.1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/2_silent_lucidity_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/2.2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/3_free_as_a_bird_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/3.1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/3_free_as_a_bird_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/3.2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/4_a_little_bit_of_soap_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/4.1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/5_heart_shaped_box_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/5.1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/5_heart_shaped_box_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/5.2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/6_people_got_to_be_free_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/original/6.1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/original/6_people_got_to_be_free_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume" preload="metadata"><source src="/assets/for_projects/m2l/audio/original/6.2.mp3" type="audio/mpeg"></audio> |
| AI-Lyricist | [sheet](/assets/for_projects/m2l/sheets/lyricist/1_faded_love_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/1_faded_love_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/2_silent_lucidity_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/2_silent_lucidity_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/3_free_as_a_bird_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/3_free_as_a_bird_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/4_a_little_bit_of_soap_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/5_heart_shaped_box_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/5_heart_shaped_box_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/6_people_got_to_be_free_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/lyricist/6_people_got_to_be_free_p2.pdf){:target="_blank"} |
| SongMASS | [sheet](/assets/for_projects/m2l/sheets/songmass/1_faded_love_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/1_faded_love_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/2_silent_lucidity_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/2_silent_lucidity_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/3_free_as_a_bird_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/3_free_as_a_bird_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/4_a_little_bit_of_soap_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/5_heart_shaped_box_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/5_heart_shaped_box_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/6_people_got_to_be_free_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/songmass/6_people_got_to_be_free_p2.pdf){:target="_blank"} |
| BART ft. | [sheet](/assets/for_projects/m2l/sheets/bart_ft/1_faded_love_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/1_faded_love_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/2_silent_lucidity_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/2_silent_lucidity_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/3_free_as_a_bird_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/3_free_as_a_bird_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/4_a_little_bit_of_soap_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/5_heart_shaped_box_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/5_heart_shaped_box_p2.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/6_people_got_to_be_free_p1.pdf){:target="_blank"} | [sheet](/assets/for_projects/m2l/sheets/bart_ft/6_people_got_to_be_free_p2.pdf){:target="_blank"} |
| Unsupervised | [sheet](/assets/for_projects/m2l/sheets/unsupervised/1_faded_love_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-1-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/1_faded_love_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-1-2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/2_silent_lucidity_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-2-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/2_silent_lucidity_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-2-2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/3_free_as_a_bird_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-3-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/3_free_as_a_bird_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-3-2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/4_a_little_bit_of_soap_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-4-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/5_heart_shaped_box_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-5-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/5_heart_shaped_box_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-5-2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/6_people_got_to_be_free_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-6-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/unsupervised/6_people_got_to_be_free_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/unsupervised/6-6-2.mp3" type="audio/mpeg"></audio> |
| Ours | [sheet](/assets/for_projects/m2l/sheets/ours/1_faded_love_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-1-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/1_faded_love_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-1-2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/2_silent_lucidity_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-2-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/2_silent_lucidity_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-2-2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/3_free_as_a_bird_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-3-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/3_free_as_a_bird_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-3-2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/4_a_little_bit_of_soap_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-4-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/5_heart_shaped_box_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-5-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/5_heart_shaped_box_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-5-2.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/6_people_got_to_be_free_p1.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-6-1.mp3" type="audio/mpeg"></audio> | [sheet](/assets/for_projects/m2l/sheets/ours/6_people_got_to_be_free_p2.pdf){:target="_blank"}<br><audio controls controlsList="nodownload noplaybackrate" class="no-volume"><source src="/assets/for_projects/m2l/audio/ours/4-6-2.mp3" type="audio/mpeg"></audio> |

</div>
