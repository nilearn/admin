---
title: Nilearn developers meeting
tags: [Nilearn]

---

---
title: Nilearn developers meeting
---

# Nilearn developers meeting

## Important links

- Jitsi link: https://meet.jit.si/nilearn-dev-team-meeting
- dev on-boarding doc: https://hackmd.io/PPAjvZ0SSzeJeeqRIhWmNA?both=

```markdown    
<!-- TEMPLATE TO COPY PASTE -->

## Month day year

**Attending:**

- Elizabeth
- Bertrand
- Hao-Ting
- Remi
- Himanshu
- Nicolas
- Michelle
- Mohammad
- Taylor
- Jérôme
- Alexis

### News

### Issues

#### number - title

### PRs

[List of PR for discussion](https://github.com/nilearn/nilearn/issues?q=label%3A%22Next%20dev%20agenda%22%20)

[List of PR needing review](https://github.com/nilearn/nilearn/pulls?q=is%3Apr+is%3Aopen+label%3A%22Review+required%22)

#### number - title

### Set time next meeting
```

## November 5th 2024

**Attending:**

- Elizabeth
- Bertrand
- ~~Hao-Ting~~
- Remi
- Himanshu
- ~~Nicolas~~
- Michelle
- Mohammad
- ~~Taylor~~
- Jérôme
- ~~Alexis~~

### News

- new core dev: Michelle and Mohammad interested in joining. Added to our private google cal.
- hacktoberfest debrief: [a few PRs merged](https://github.com/nilearn/nilearn/pulls?q=is%3Apr+is%3Aclosed+label%3Ahacktoberfest-accepted) - may lead to extra work for maintainers but allows to tackle things that we would not have had the bandwidth for. No 'spam' PR but more PR that looked AI generated.
    - Try to avoid planning a release for Hacktoberfest if participating in the future
- [youtube channel](https://www.youtube.com/@nilearnevents5116/videos): add to footer of doc and added a [youtube playlist](https://m.youtube.com/playlist?list=PLrrL5W8SkvZU5IKgkrbL7SHDpiIiVybOR) to curate nilearn videos not made by us  

### OHBM

- who is going?
    - Michelle and Himanshu are possibly going this year
- should we prepare a poster?
    - Himanshu will take point on this: poster should decribe what's in release 0.11
    - deadline 17th Dec

### Release 0.11

- milestone: https://github.com/nilearn/nilearn/milestone/26
- roadmap: https://github.com/orgs/nilearn/projects/4/views/3

#### WIP

##### Moving API

- moving API: see [meta-issue](https://github.com/nilearn/nilearn/issues/4568)
  -  moving maskers and datasets is in progress
  -  moving of SurfaceImage classes to be done last
- moving example: one example would probably be better merged into the others: https://github.com/nilearn/nilearn/pull/4684 
    - to be put in https://nilearn.github.io/stable/auto_examples/07_advanced/index.html

##### MUST DO

PRs that MUST be finished before the release

- [[ENH] make the number of vertices the first dimension of image data](https://github.com/nilearn/nilearn/pull/4591)

##### Nice to have ?

PRs that are started but that may be not necessary for the release

- [[ENH] Allow to run clustering on SurfaceImage](https://github.com/nilearn/nilearn/pull/4577)
    - could be handled in a future release
- [[DOC] Surface API explainer](https://github.com/nilearn/nilearn/pull/4665)
    - ready for review
- [[ENH] Handling of SurfaceData in compute_contrast](https://github.com/nilearn/nilearn/pull/4610)
    - ready for review
    

#### TODOs

Some issues have not been started yet.
Wonder if some could be dropped from the scope of the next release.

- [support 2nd level GLM analysis of SurfaceImage objects](https://github.com/nilearn/nilearn/issues/4617)
- [modify experimental example Surface-based first and second level analysis to show how to project images to volume](https://github.com/nilearn/nilearn/issues/4642)
- [update surface searchlight to run with the new SurfaceImage](https://github.com/nilearn/nilearn/issues/4654)
    - BT: check how much work it is
    - Himanshu: to check the (IBC) surface dataset on osf and create an issue for that
- [adapt add_contours (plotly) to accept SurfaceImage objects](https://github.com/nilearn/nilearn/issues/4691)
- [[BUG] SurfaceMasker does not take list of Surface images](https://github.com/nilearn/nilearn/issues/4592)
    - to be addressed after #4591

#### Decisions

- Evaluate next week if we can get the release out by **15 November** with current point people, or if we need to further delegate

### Issues

#### simple syntax in examples ?

- avoid some 'advanced' python syntax in the examples to be more beginner friendly (especially if they do not exist in other languages from our community like R or matlab)
- some examples from the top of my avoid list, dict... comprehensions, avoid +=, -=... operators
- see [comment](https://github.com/nilearn/nilearn/pull/4704#discussion_r1827463392)

#### Decisions

- Disassociate tracking ruff from applying to the example section
    - Example syntax can be managed separately to be "beginner friendly" rather than "best practice"
    - Don't track ruff-preview releases; for now, only plan for stable ruff releases

### PRs

[List of PR needing review](https://github.com/nilearn/nilearn/pulls?q=is%3Apr+is%3Aopen+label%3A%22Review+required%22)

#### [4707 - [STY] apply US spelling](https://github.com/nilearn/nilearn/pull/4707)

 low effort standardization. Anyone feels strongly about this?

### Set time next meeting

December ???


## October 1rst 2024

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- ~~Jérôme~~
- ~~Alexis~~
- Hao-Ting
- ~~Taylor~~
- Remi
- Himanshu

### Reminder: Hackathon on Friday

Goal: 'dressed rehearsal' of the Surface API to see if it's ready from prime time.

Rémi: I will be "on" for most of the day, so that people can drop by at any time and I will try to prepare 'tracks' for 'things to do/review if I have 30 minutes / 1 hour / 3 hours'.

#### Advertise hackathon

- twitter and others...
- tell Hande

### News:

#### hacktober fest

Rémi: we could try to add Nilearn to the pool of repos that participate to the next hacktoberfest. From our side it requires adding a tag to the repo and some extra labels to the issues / PR that are involved in the hacktoberfest. I have a few issues in mind whose wording I could improve to make them more explicit on what is required.

More info here: https://hacktoberfest.com/participation/#maintainers

**ACTION**: let's try it and see if we are flooded with SPAM

#### 2 nilearn google calendar to track public and private events

Rémi: You should have received emails to give you "write" access to both. Let me know if you did not receive anything or if I should add another email address for you. @Elizabeth I also added the nilearn.events@gmail.com as one of the admin (I think you are in control of it, right?).
 
  - public: https://calendar.google.com/calendar/embed?src=87f409f6c8543a93a45d4c136e011abe6bcf78adfc1bbf665fc3bd2f8bb0f5ba%40group.calendar.google.com&ctz=Europe%2FParis

  - private: https://calendar.google.com/calendar/embed?src=945ae93030a36f912a00a67b1d752141a3dc50cc05b6de46bc2af3ab66a081d5%40group.calendar.google.com&ctz=Europe%2FParis

#### Youtube channel

Rémi: I am not sure but this looks like the "official" channel, no?

https://www.youtube.com/@nilearnevents5116/videos

Is this linked to the nilearn.events@gmail.com address ? @Elisabeth do you know?

Would probably be good to reactivate it and at least create a playlist that centralizes all the talks, demo


#### New issue label

Rémi: I have been trying to do a bit of issue triaging. I added a a new "help wanted" label to denote issues where we explicitly ask for help from the community but that may not be for "first timers": not 100% sure if this is very useful but decided to add and see if it at least helps us.

https://github.com/nilearn/nilearn/labels/Help%20wanted

**ACTIONS**:
- remove label - not clear enough
- make a help "wanted column" in the nilearn generic project
- make projects public

#### codetriage

Rémi: talking about triaging. Has anyone used code-triage? https://www.codetriage.com/what Came across it on the pytest repo. It seems to be a way to engage people who would like to contribute to a project but not necessarily with code. If you subscribe to a repo you get emails with issues from that to help "triage", confirm if it is a bug report, validate... Seems like a less intimidating way for people to start jumping into the whole github thing. Should we add it on the Nilearn README?


### Issues

- Too many... I don't even know where to start... :stuck_out_tongue_winking_eye: 


### PRs

- Several PRs need at least one or 2 reviews: [List of PR needing review](https://github.com/nilearn/nilearn/pulls?q=is%3Apr+is%3Aopen+label%3A%22Review+required%22)
  - get more maintainers: Mohammad Torabi, Michelle Wang, PL Barbarant
- python 3.13
  -  python can now be free-threaded with no global interpreter lock (GIL)
  -  Should we run tests for this as well?
  -  https://github.com/nilearn/nilearn/pull/4513
  -  is it enough to have our dependencies do it:
    - sklearn: 
      - https://dev.azure.com/scikit-learn/scikit-learn/_build/results?buildId=70481&view=logs&j=8bc43b48-889f-54b9-cd8b-781ee8447bf2  
      - https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aissue+is%3Aopen+3.13
  - **ACTION**: check joblib as well 


### Set time next meeting
 
November Tuesdays: 5th 4PM UTC 
 
### Grant

- CZI
- connect to giga connectome


## August 27th 2024

**Attending:**

- ~~Elizabeth~~
- ~~Nicolas~~
- Bertrand
- ~~Jérôme~~
- Alexis
- Hao-Ting
- ~~Taylor~~
- Remi
- Himanshu

### News

- Remi switching from ORIGAMI lab to INRIA

### Issues

- Next steps for development on experimental surface module https://github.com/nilearn/nilearn/issues/4027
  -  Missing
    - decoder: https://github.com/nilearn/nilearn/pull/4205 
      - ACTION: cross check that ready for merge
    - BIDS compatibility: https://github.com/nilearn/nilearn/pull/4507
      Shape of data in SurfaceImage: https://github.com/nilearn/nilearn/pull/4507#discussion_r1722167540

    - GLM report: https://github.com/nilearn/nilearn/pull/4442
    - Doc and user guide update: https://github.com/nilearn/nilearn/pull/4442
  - To discuss: 
    - date for the next release
      - not September
      - preferably in late October 
    - scope: are all of the above required?
      - BIDS and GLM report not required (nice to have)
      - not the doc / user guide, should not be blocker
    - Integrate experimental surface as stable in the next release?
      - Plan an internal hackathon (preference on Friday) 
      - 4th October
    - What to deprecate from old surface.py API?
      - Yes 

### PRs

- HTML report for tests: https://github.com/nilearn/nilearn/pull/4486
  - are we OK having those ? If yes needs a second positive review

- return 3D effect maps for t contrasts:  https://github.com/nilearn/nilearn/pull/4439
  - must fix for next release
  - @bertrand: should I assign to you? 

- support GLM on numpy arrays directly: https://github.com/nilearn/nilearn/pull/4112

### If we have time

Can be turned into issues for later discussions

#### version 1.0.0 release ?

Mentioned by Chris M as a side conversation.

What's holding us back from a version 1.0.0?
What would we consider required for 1.0.0?

- more like after Surface is stabilized

#### Add analytics to the docs

To help us know which parts are more looked at so we know where to focus our efforts.

[plausible](https://plausible.io/) seems to be a potential alternative to google analytics.

#### google agenda for meetings / open office hours ?

see if we can use the nilearn.events@gmail.com


### Next month
- (Himanshu) Vacation until 28th Sep
- Next meeting Oct 1st

## July 2nd 2024

**Attending:**

- ~~Elizabeth~~
- ~~Nicolas~~
- Bertrand
- Jérôme
- ~~Alexis~~
- ~~Hao-Ting~~
- ~~Taylor~~
- Remi
- Himanshu

### Brainhack/OHBM 2024
- Lots of love for docs and examples
- Plotting and GLM most popular
    - hyve: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11042383/
    - push NiiVue backend?
    - unthresholded stat maps with varying alpha in the colormap:
      - https://github.com/nilearn/nilearn/issues/3789
- Specify "fMRI" or atleast "MRI images" instead of "brain images" in tagline
- a few people wanted to use deep models for decoding
    - consider using skorch

### Other
- merge policy: 2 positive reviews from core-devs
- summer hiatus for office hours
    - stop from next week, back on 4th Sep
- Remi: will be less responsive till 19th july

### PRs
- https://github.com/nilearn/nilearn/pull/4486
- https://github.com/nilearn/nilearn/pull/4444#issuecomment-2188889063

### Issues
- https://github.com/nilearn/nilearn/issues/4401

### Priorities for the next month
- (Himanshu) Decoding example
- (Himanshu) Catch up with Alexis for NiiVue PR: https://github.com/nilearn/nilearn/pull/3729
    - update the niivue in surface PR
    - later replace plotly with niivue for 3d plots
    - look into saving pngs with niivue (kaleido does this for plotly)
- Next meeting poll between 13th, 20th, 27th Aug


## May 28th 2024

**Attending:**

- ~~Elizabeth~~
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- ~~Hao-Ting~~
- ~~Taylor~~
- Remi
- Himanshu

### OHBM 2024, Seoul (23-27 June)

- Attending? 
  - Yes: Himanshu, Elizabeth
  - No: Rémi, Bertrand, Hao-Ting, Jérôme
- Poster:
  -  about surface API
  -  poster from last year: https://drive.google.com/drive/folders/1HmyEnCksdQ2aoX6IyN5PS4ee1IcecJQZ?usp=drive_link
  -  abstract : https://drive.google.com/drive/folders/10Mxj9f6UYh7VYxx4gCDDeHjSHUbi7FDR?usp=drive_link 
  -  push previous years posters and abtracts to github

- BrainHack 2024 (20-22 June) Project: 
    - https://ohbm.github.io/hackathon2024/
        - open issue
        - identify easy issues to "prepare" for potential new contributors

### PR

- Header PRs: 
    - Deprecation cycle? `nilearn.image` API change to copy headers by default https://github.com/nilearn/nilearn/pull/4397
        - open another PR that adds a warning message
        - update in 0.13.0
    - Example to show header copying with `math_img` https://github.com/nilearn/nilearn/pull/4392
        - move under advanced examples
        - show a rendered HTML in the PR
        - ping people for a review

### Issues

- Adding cyclic analysis to `nilearn.connectome.ConnectivityMeasure`:
  https://github.com/nilearn/nilearn/issues/4124
  code snippet: https://gist.github.com/iabraham/3948d23417bf11e6933833b1e17ea7d4
  We may not have the bandwidth or the expertise to maintain this.
  Implement a way to for users to "plugin" their own connectivity estimator? Maybe more effort than it is worth.
  Advise to keep this kind of development / implementation in a separate fork.
  Could revisit the issue if more users ask for it.
  
- Demonstrate inner workings of `nilearn.Decoder` via sklearn: https://github.com/nilearn/nilearn/issues/4344
    - another goal is also to provide reasoning for choices made

## Priorities for the next month

-  Rémi:
  -  Fix CI for doc building
  -  Get back to Surface API

## March 26th 2024

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- ~~Taylor~~
- Remi
- Himanshu

### Agenda

### Meeting with niivue

- Chris Rorden 

- link to slides : https://docs.google.com/presentation/d/1pWVk53cofExuT4mF1qffaZflIu3kP5pIkfd_hxRaG5o/edit?usp=sharing

Related issues / PR:

- https://github.com/nilearn/nilearn/issues/3451
- https://github.com/nilearn/nilearn/pull/3729
- https://github.com/nilearn/nilearn/pull/4235

---

- Assumptions on file formats?

  - https://github.com/niivue/niivue?tab=readme-ov-file#supported-formats
  - try to support format used by for most of the big tools 
  - connectome is the only format where new formats have had to be created

- work to be done on the niivue front to polish python even more to make it easier for nilearn users (but also the python community as a whole).

- next steps:
  - support directly for the new nilearn object for surfaces?
  - integrate niivue engine first and then expand to the new nilearn objects?

- Passing objects to niivue should probably be done by at least an intermediate step where objects are "saved on disk". Would help decouple our surface object representation from the their plotting.

- JS API is fairly stable as it is used by several big tools who want to keep the API stable.

- ACTION: plan a meeting to go through [#3729](https://github.com/nilearn/nilearn/pull/3729) with Alexis, Himanshu, Remi and people from the niivue team to improve python interface API.

#### 0.10.4 release

Bug fix release "only".
Was supposed to be for a couple of bugs due to 0.10.3, but has been delayed from end of February because new bug reports have been coming in (not all from 0.10.3).

-  0.10.4 Release at the end of the month (for sure this time)

- fix CI errors for numpy2 compatibility and other workflows that fail
  - https://github.com/nilearn/nilearn/issues/4309
  - https://github.com/numpy/numpy/issues/24300

- Need to bring back in dev meetings:
  - issue prioritizing 

#### coding sprint, brainhack

- OHBM: who will go?
- Brainhack Montreal: who would go? (for budgeting)

#### version 1.0.0 release ?

Mentioned by Chris M as a side conversation.

What's holding us back from a version 1.0.0?
What would we consider required for 1.0.0?

#### Add analytics to the docs

To help us know which parts are more looked at so we know where to focus our efforts.

[plausible](https://plausible.io/) seems to be a potential alternative to google analytics.

#### google agenda for meetings / open office hours ?

#### dev on-boarding doc

https://hackmd.io/PPAjvZ0SSzeJeeqRIhWmNA?both=


## February 13th 2024

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- ~~Yasmin~~
- ~~Taylor~~
- Remi
- Himanshu

### Agenda

- Introduction of Himanshu
    - TODO: Rémi to help with on-boarding

- What actions to undertake with the wide community:
    - coding sprint, brainhack ?
    - Before/after OHBM ?
    - or another conference ?
        - brainhack in October
        - OHBM in June in Seoul, but only few people attend ; maybe a hackathon before
    - make it a docathon ? Reaching experts of Nilearn topics
    - EMD : @Remi probably worth checking with @JB to make sure he didn't have any events planned to use that CZI allocation for events ; I think that resets in June 


- Bug fix release at the end of the month?
  - **Needs review:** https://github.com/nilearn/nilearn/pull/4256 
  - **Relates to:** https://github.com/neurostuff/NiMARE/actions/runs/7749170814/job/21133189716
  - (Tangentially-related issue: https://github.com/neurostuff/NiMARE/issues/872)

- Technical discussions
    - surface module:
        - meta-issue: [4027](https://github.com/nilearn/nilearn/issues/4027)
          - [plotting and design choices: 4235](https://github.com/nilearn/nilearn/pull/4235): Blocker
          - Implement GLM report: Blocked by 4235; Blocker for 4126
          - [GLM: 4126](https://github.com/nilearn/nilearn/pull/4126)
          - [decoding: 4205](https://github.com/nilearn/nilearn/pull/4205)
          - [Move API: 4229](https://github.com/nilearn/nilearn/pull/4229)

Next time:  March 26th
Suggestion to invite Niivue people (Alexis contacts them)

## January 19th 2024

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- ~~Taylor~~
- Remi
- Chris (Nibabel)


#### General

- Nibabel CoordinateImage API discussion w/ Chris

    - suggestions:
        - add "header" as a metadata dict as will be required for saving to files
        - if Nilearn surface interface is meant in the long term be just a wrapper on Nibabel Surface class then we could limit ourselves to only track the data we need and let users access metadata once we wrap around Nibabel
        - filename templates:
            - .surf.gii
            - .func.gii
        - nibabel timeline: no specific ETA
            - only pointset finished so far

- Nilearn 0.11 release

    - https://github.com/nilearn/nilearn/milestone/24
    - Check on 26/01 if we have enough for a stable release with surface API
    - Another option is to do a minor 0.10.3 release and follow-up with a major release in a few months when surface is ready

- Admin tasks
    - recap: https://github.com/nilearn/admin/blob/main/admin/admin_info.md
    - Planning drop in hours (Rémi for now)
        - Tweet office hours
        - Reminder email sent the day before from the nilearn gmail account with a link 'who can be there' spreadsheet.
        - Consider making better use of discord / neurostars ?
    - Coredev meeting planning (Bertrand)
        - Keep next one planned for Feb 13
    - Who needs access to twitter and mastodon?
        - transfer accounts to the nilearn gmail account
    
- New job: need for another round of ads?
    - not for now


##### Access to accounts on OSF
See this one: https://osf.io/4r3jt/

What about this nistats project that hosts some of our datasets?
https://osf.io/v7hsw/?view_only=

And this one: https://osf.io/5dr8p/?view_only=
that mirrors this one: https://osf.io/k4jp8/ while download from that address is failing.

**DECISION:**

- centralize all datasets on OSF under the nilearn OSF account
- make sure that that all devs have access to the projects
- update admin info for future on boarding

##### Add BIDS dataset with more recent fmriprep ?

- https://github.com/nilearn/nilearn/pull/4198
- must have rest and task fMRI (ideally a task wiht event related design with several runs to decode on)
- Hao-Ting's downsampled datasets?
    - ds000228 (rest/movie watching, not uploaded yet)
    - [ds000017](https://zenodo.org/records/7901637#.ZFWJ15HMI4s) (task, on zenodo) 
- other possibility update examples we have to rename files / TSV where header where ncessary to fit our needs

**DECISION:**

- Rémi to open an issue for planning this




## December 12th 2023

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- ~~Taylor~~
- Remi

### Agenda

#### General
    
- Release milestones
    - https://github.com/nilearn/nilearn/milestone/24
    - surface code out of experimental, so that using glm does not trigger the issue

    - taking Surface out of experimental
        - no feedback on it but we did not have any explicit "useful" feature
        - wait for more feedback and feature until we are confident ?
        - or merge "soon" (before the release) the GLM surface PR and take the new Surface feature out of experimental ?
        - few people use surface for GLM so we may not get a lot of "signal" from them
        - DECISION: do not take a decision today but let's take a decision soon (before Xmas)

 - Update on surface API
    - https://github.com/nilearn/nilearn/issues/4027
    - https://github.com/nilearn/nilearn/pull/4126 (need review)
    - What else is needed?
        - examples?
        - visualizations?
            - Forcing 'left' and 'right' keys
    - Comments on Chris M. comments

> I would be interested in your takes on https://github.com/nipy/nibabel/pull/1257. Since last I posted, the Pointset base class was merged, but TriangularMeshes having two arrays and possibly a family of associated coordinates feels a bit trickier to get right. With your experiences with your own structures, I want to know if the proposed class looks like it would be easy/difficult to work with, or what tests you'd want to see to make that determination.


#### Open issues and PRs

- Bugs
    - https://github.com/nilearn/nilearn/issues/3807 and https://github.com/nilearn/nilearn/issues/4140 and PR https://github.com/nilearn/nilearn/pull/4150 (need reviews)
        - Decide if we want to support or not
    - https://github.com/nilearn/nilearn/issues/4087 and PR https://github.com/nilearn/nilearn/pull/4116 (need help)
        - Hai-Ting will review

#### CZI EOSSS 2022 - GLM

Kanban board of TODOs from the CZI EOSSS grant

https://github.com/orgs/nilearn/projects/11/views/2?pane=issue&itemId=46168608

Relating to GLM performance:
- one bottleneck seems to be the masking step
  - better benchmark / profiling could help
  - https://github.com/nilearn/nilearn/issues/3398
  - https://github.com/nilearn/nilearn/issues/3399 
- possible optimization: pre-compute 
- improve documentation with a page of tips regarding large scale analysis
    - Hao-Ting and members of lab have some pointers on this

#### For next meeting

Invite Nibabel dev team to join us. (Yasmin emailed)

## November 14th 2023

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- ~~Yasmin~~
- ~~Taylor~~
- Remi

### Agenda

#### General

- OHBM abstract review
    - Delayed deadline Dec 1st
    - https://docs.google.com/document/d/1BuuZMEm0wM2v-ZgKr-8RtAyKS0WINltOA4DC3oZYjM8/edit
    - The abstract looks mostly good. Could be improved by adding a second figure. Maybe a flatmap ?
- Surface API sprint (Nov 24, 14h - 17h UTC)
    - Location in Paris: Inria Paris la salle Georg Cantor (batiment C)
        - Can announce on twitter/mastodon
    - Online: discord or jitsi? -> Discord is preferred
    - Existing issue : https://github.com/nilearn/nilearn/issues/4027
        - Gdoc for editting : https://docs.google.com/document/d/1Hj5Gnk1kreTZ2vZixP_wVMnCZhvXadwfFN02KFvoNoQ/edit?usp=sharing
        - Have GLMs and Decoders to work seamlessly with SurfaceImage of NiftiImage
    

#### Open issues and PRs



## October 24th 2023

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- ~~Taylor~~
- Remi

### Agenda

#### General

- DOI
    - Include Zenodo ROI in Readme
    - Also reference for OHBM poster
    - Which reference for nilearn
        - one for releases represents all contributors
    - https://github.com/nilearn/nilearn/pull/4032
    - **DECISION**: use the zenodo DOI as the main one.
- Major release
    - start adding type hints: 
        - https://github.com/nilearn/nilearn/issues/3568
        - https://github.com/nilearn/nilearn/pull/3569
        - Handling typing for docstrings (see #4049 linked below)
        - **DECISION**: let's wait a bit 
    - when do we drop 3.8?
        - Currently planned for release 0.12 (dep warning)
        - EOL (Oct 2024)
        - **DECISION**: drop warning about python version completely
- OHBM abstract
    - Nov 17th
    - draft: https://docs.google.com/document/d/1BuuZMEm0wM2v-ZgKr-8RtAyKS0WINltOA4DC3oZYjM8/edit
    - Send to all contributors for feedback
- Review policy: need 2 approvals for merge
    - **DECISION**: make the policy explicit by requiring 2 approvals on github (no reapproval required, admin can override).
- Think about planning another sprint for reworking the user guide
    - https://github.com/nilearn/nilearn/issues/3379
    - Try to set up before spring

#### Open issues and PRs

- Surface
    - **DECISION**: sprint on the 24th of November to make progress
        - Yasmin sends an invite
    - https://github.com/nilearn/nilearn/issues/4027
    - https://github.com/nilearn/nilearn/pull/4049
        - issue https://github.com/nilearn/nilearn/issues/4018
    - *Side note*: plan a sprint in the spring
- Atlas proposals
    - **DECISION**: 
        - make it more obvious in the doc and easier to link to
        - mention it in the auto reply to PRs (or issues)
        - point users to other "imperfect" solutions
    - https://github.com/nilearn/nilearn/issues/4039
    - https://github.com/nilearn/nilearn/issues/4074
    - See also older similar issues:
        - https://github.com/nilearn/nilearn/issues/1167 
        - https://github.com/nilearn/nilearn/issues/2273
        - doc needed: https://github.com/nilearn/nilearn/issues/3075
        - general fetcher: https://github.com/nilearn/nilearn/issues/3086
        - deprecate fetchers: https://github.com/nilearn/nilearn/issues/3086
- Default values
    - https://github.com/nilearn/nilearn/pull/4040#discussion_r1350250330
    - **DECISION**: default in "type" section of the docstring should match what appears in the function definition. If `None` is passed and another value is set in its place then it should be described in the "description" of the docstring.


## September 12th 2023

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- ~~Taylor~~
- Remi

### Agenda

#### General

- Surface API PR https://github.com/nilearn/nilearn/pull/3856
    - Review comments
        - PR almost ready to merge
            - Add warnings
            - Try to increase maskers tests if it makes sense
            - Deal with flake8
    - Consider adding limited cifti case (see fitlins) - nothing prevents from future integration of cifti
        - User should know space data is in (don't deal with wbspec)
        - CIFTI_MODEL_TYPE_SURFACE
        - CIFTI_STRUCTURE_CORTEX_LEFT/CIFTI_STRUCTURE_CORTEX_RIGHT
        - dscalar.nii, dtseries.nii?
    - Merge PR before next minor release with copious amount of warning to let users know about the experimental nature of this feature and API
    - Jerome to open an an issue listing the follow-up steps after the merge
- TODO before minor release end of September
    - https://github.com/nilearn/nilearn/milestone/25
    - Finish PR for order of contributors (consortium authorship + alphabetical order)
    - Then do Zenodo release

#### Open issues and PRs



## June 20th 2023

**Attending:**

- Elizabeth
- ~~Nicolas~~
- ~~Bertrand~~
- Jérôme
- ~~Alexis~~
- Hao-Ting
- Yasmin
- ~~Taylor~~
- Remi

### Agenda

#### General

- Nilearn at OHBM
    - OHBM brainhack - https://hackmd.io/5gwxDYHiQ_iNCT3klzqp7g
        - Back up projects for first timer 
        - Filter first timer issues and prioritise surface
        - Invite Mohammad and Michelle to the next office hour (28 June) to discuss the scope of tasks
    - Poster
        - Yasmin working on this and will circulate for feedback
- Surface API planning
    - What needs to be done to merge https://github.com/nilearn/nilearn/pull/3473/ ?
        - Reference: https://nipy.org/nibabel/devel/biaps/biap_0009.html
        - Focus on Gifti support rather than coordiante image as we don't need 
    - Project board: https://github.com/orgs/nilearn/projects/4/views/1
    - "roadmap": https://github.com/nilearn/nilearn_sandbox/blob/master/discussion/surface_api_office_hours_2022-10-14/surfaces_draft.md
    - Yasmin will work on the surface loader
        - Leave CoordinateImage API for now but try to stay consistent
- ancp-bids / PyBIDS proposal https://github.com/bids-standard/pybids/issues/989
  - improve documentation on what our current BIDS handling functions do and do not do
  - not necessariy urgent ; we have "stop-gap" code that we have been using for a couple of years
  - long term goal is to delegate BIDS handling to an external library
  - feed back on RFC what exactly we're using in the library right now
    
- internal communication: 
    - "core devs" channel on our discord server
    - make all core devs admin of the server
- fixed date for yearly major release: January - **Discuss again next meeting**
  - goal: 
    - help us plan / organize
    - help users when to expect new features / deprecations
      (deprecation warnings send to a "roadmap" page) 
  - future releases
    - 0.11: Jan 2024
      - drop python 3.7
      - enhanced surface support
    - 0.12: Jan 2025
    - 0.13: Jan 2026
  - previous releases 
    - 0.10: Jan 2023
    - 0.9: Jan 2022
    - 0.8: Jun 2021
    - 0.7: Nov 2020
    - 0.6: Dec 2019
    - 0.5: Nov 2018
    - 0.4: Nov 2017
    - 0.3. Nov 2017
    - 0.2: Dec 2015
    - 0.1: Feb 2015
- Can anybody attend drop-in hour tomorrow?
  -  Rémi : Can't

#### Open issues and PRs

## June 12th 2023

### Nilearn: priorities and roles

- use discord
    - channel only for coredevs (can be public) to quickly address small things
- develop roadmaps for our different long term goals
    - BIDS
    - surface
- set up a kanban board to organize priorities and get an idea of who is doing what


## May 16th 2023

Meeting cancelled

**Attending:**

- Elizabeth
- Nicolas
- Bertrand
- Jérôme
- Alexis
- ~~Hao-Ting~~ (can look for a office hour to discuss hackathon)
- ~~Yasmin~~
- ~~Taylor~~
- Remi

### Agenda

#### General

- OHBM sprint topics:
    - User Guide
- ancp-bids / PyBIDS proposal https://github.com/bids-standard/pybids/issues/989

#### Open issues and PRs


## April 18th 2023

**Attending:**

- ~~Elizabeth~~
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- ~~Taylor~~
- Remi

### Agenda

#### General

- Discuss BIDS scope in nilearn [**Move to next meeting**]
    - Rémi: maybe better postpone the discussion when Elizabeth is here?
    - [Related issue](https://github.com/nilearn/nilearn/issues/3567)
    - Keep an eye out for PyBIDS possibly merging ANCP-BIDS into codebase
- Organising a sprint / dev days
    - try to tag it along another community event (OHBM hackaton, a specific brainhack)
    - Contact this year: Anibal (anibalsolon@gmail.com); Hao-Ting make the request
    - Go through the user guide to spot things to be improved
- Minor release for end of April
- Release process - standard practice or stick to monthly prerelease?
    - If standard:
        - Given the way we version, more patch ("minor") releases for bugfixes
        - 1 major release per year will be much bigger in terms of changes
            - Can do 2 instead
            - And use prereleases for their intended purpose
    - Decision to stick to previous way of making releases (no monthly prereleases)
    - Going standard is much more work with working with several branches
- Put some effort on Surface handling https://github.com/nilearn/nilearn/pull/3473
    - Plan another drop-in hour with Chris (Yasmin will email)
    - Can also discuss amongst ourselves during one of the drop-in hours 
- Formatting/refactoring related:
    - Misunderstanding about default parameters decision: https://github.com/nilearn/nilearn/pull/3621
        - Stick to decision of moving default values to the type definition of parameters 
    - `__init__.py` in test suite: https://github.com/nilearn/nilearn/issues/3660
        - change name of issue to "using a source layout" 
        - readd __init__.py that were deleted
    - Private function naming https://github.com/nilearn/nilearn/issues/3628
        - if a function starts with "\_" it is private to that module 

- LabelsMasker https://github.com/nilearn/nilearn/issues/3085
    - Go with first option of deprecating old behavior (needs 2 separate deprecation cycles)
- NiiVue update
    - Some surface plotting functionality can already make use of niivue engine
    - We can focus on surface plotting first and keep brainsprite for volumetric data
    - Consider how to save PNG of a view
    - NiiVue is not as well tested as plotly and the documentation can be improved
    - Plotly uses up a lot of memory and has some rendering issues
    - See issue [#3451](https://github.com/nilearn/nilearn/issues/3451) for prototypes for integration into nilearn

#### Question

- ever had the need for an interface to "query" SPM.mat files?
  - get design matrix, file name for beta image for a condition...

- nilearn montly stats on neurostars

collected via the discourse API with this script: https://github.com/bids-standard/maintenance-tools/blob/main/neurostars.py

- Add script to nilearn/nilearn_sandbox

| nb_topics | new_topics | nb_posts | new_posts | topics_with_no_reply | topics_with_accepted_answer | mean_nb_post_per_topic  | percent_no_reply |	percent_accepted_answer  |
| - | - | - |	- |	- |	- |	-  | -  | -  |
| 441 | 7 | 1902 | 28 |	62 | 127 | 4.3 | 14.0 | 28.7 |	

#### Open issues and PRs


## March 21st 2023

**Attending:**

- Elizabeth
- Nicolas
- Bertrand
- ~~Jérôme~~
- Alexis
- Hao-Ting
- Yasmin
- Taylor
- Remi (remi.gau@gmail.com)

### Agenda

#### General

- Make decision about default parameters
    - See discussion in [#3519](https://github.com/nilearn/nilearn/issues/3519)
        - Add them to the doc string, along with the type but not at the end of the doc string.

- Adding type annotations to Nilearn [#3568](https://github.com/nilearn/nilearn/issues/3568)
    - See also [mypy PR #3569](https://github.com/nilearn/nilearn/pull/3569)
        - finish with reformating before adding type annotations to the whole codebase
        - maybe not type the whole codebase
        - Revisit in a few months

- Refactoring unit tests
    - Discuss guidelines, see [comment](https://github.com/nilearn/nilearn/pull/3572#issuecomment-1458028646)
        - add doc strings to help give an overview of what / why / how things are tested
        - can be done iteratively 
        - make sure new tests have explanation

    - Refactoring `nilearn._utils.data_gen`, see [comment](https://github.com/nilearn/nilearn/pull/3572#issuecomment-1468620089)
        - if the data gen is just used just for one module, keep it in that module
        - otherwise if the scope is bigger move it to  `nilearn._utils.data_gen`

- Updates about moving to `pyproject.toml`
    - Check in with Jerome when he's available.
    - Ask Chris why nibabel still has a requirements.txt file.

- Pre-release schedule
    - Consider [comment](https://github.com/nilearn/nilearn/pull/3520#pullrequestreview-1315351292)
    - NG: Proper semantic versioning would involve pushing enhancements/new features to a branch for the next minor release, and pushing bug fixes to a branch for maintaining the current minor release series. Each bug fix would result in a new patch release, and bug fixes would need to be ported to the next minor release's branch as well.
    - EMD: What about CalVer?
    - See also MNE-python
    - Rediscuss next meeting

- Alternatives to Discord for drop-in hours
    - Common for at least one person to have issues
    - Move to jitse but keep maintaining Discord for use in other events

- Asia Pacific drop-in hour didn't work
    - Try again?
    - More advertising: other channels than just twitter/mastodon
    - Set a date and then email coredevs to help spread the word

- Organising a sprint / dev days [**Discuss next meeting**]

#### Open issues and PRs

- [Autocorrelation](https://github.com/nilearn/nilearn/issues/3509) [**Discuss next meeting**]
    - Need somebody to review
- [BIDS scope](https://github.com/nilearn/nilearn/issues/3567) [**Discuss next meeting**]


## February 14th 2023

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- ~~Alexis~~
- Hao-Ting
- Yasmin
- Taylor
- ~~Remi~~

### Agenda

#### General

- How would folks feel about a 0.10.1rc1 release soon?
    - Alternatively, has anyone considered using a tool like [auto](https://github.com/intuit/auto)? I (TS) think it would be useful to make patch releases whenever a bug is fixed.
    - JD: There are good reasons to release fairly infrequently, so we don't want to make frequent patch releases.
    - We could have frequent pre-releases instead, so regular users won't deal with a lot of versions, but folks who need a specific bug-fix can pin to a release candidate.
    - Aim for once a month pre-releases, keeping current cadence of one non-pre-release every ~6mo
- Reformatting codebase with black
    - Line length (current is flake8 default of 79)
        - Readability might not improve even with longer line length
        - Not many lines' readability is affected
        - Keep as is
    - Where to put parameter default value in docstrings (See [comment](https://github.com/nilearn/nilearn/pull/3491#issuecomment-1427666952))
        - We need to ask Remi how the type annotation extraction tool (if there is one) would work.
        - Including the default value in the type description portion of the argument's docstring is numpydoc style, so this is probably a change we want to make even if we don't adopt type hinting.
    - Other?
- NiiVue progress
    - At the point that we can succesfully use niivue methods to load base64 encoded data and view in browser using html embedding
- Replacing `setup.py` and `setup.cfg` with `pyproject.toml`
    - https://effigies.gitlab.io/posts/python-packaging-2023/
    - http://ivory.idyll.org/blog/2021-transition-to-pyproject.toml-example.html
    - Jerome will configure `pyproject.toml` based on what Chris did and test it on testpypi

#### Open issues and PRs

- [Coordinate Image API](https://github.com/nilearn/nilearn/pull/3473)
    - Ping Chris to see where he is in terms of finishing the PR
    - Bertrand: idea to set up a hackathon to use the API
- [Renaming `plot_epi` function](https://github.com/nilearn/nilearn/issues/3388)
    - Suggest to close; no strong reason to change it
- [Non-aggressive denoising](https://github.com/nilearn/nilearn/issues/3497)
    - Perhaps add option to orthogonalize the noise ICA regressors w.r.t. the signal ICA regressors within `load_confounds`.
- [Autocorrelation](https://github.com/nilearn/nilearn/issues/3509) [--> Move to next month]


## January 17th 2023

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- Taylor

### Agenda

#### General

- Mastodon account created
    - ACTION ITEM: Add tagged introduction post.
    - TS: Link to account? https://fosstodon.org/@nilearn
- Niivue/ipyniivue update
    - JD: Jupyter widgets (ipyniivue) shouldn't be first step, and maybe should stay separate from nilearn. Embedding images in static pages (e.g., in examples) should be focus.
- Surface data support meeting with Chris
    - TS: Does this include CIFTI?
        - HTW: CIFTI isn't commonly used
        - JD: Out of scope for nilearn
    - Discuss proposal: https://github.com/nilearn/nilearn_sandbox/tree/master/discussions/surface_api_office_hours_2022-10-14
    - Discuss also nibabel's plans for surface data
- Nilearn projects for 2 students from JB's lab
    - Improving maskers
    - Improving decoding

#### Open issues and PRs

- [Background maps](https://github.com/nilearn/nilearn/pull/3173)
    - Alexis needs to push some updates
- [Flat maps](https://github.com/nilearn/nilearn/pull/3444) 
    - Can be reviewed after merging #3173

## December 20th 2022

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- ~~Hao-Ting~~
- Yasmin
- Taylor
- JB
- Chris Rorden
- Pierre Bellec
- Taylor Hanayik

### Agenda

##### General

- NiiVue discussion
    - https://niivue.github.io/niivue/
    - review of the points raised at the niivue project 
        - introduction to niivue
        - python API for niivue so that it can be used with nilearn
            - nilearn need to script visualization
            - callbacks (need for a niivue server?)
    - next steps
        - show some examples with niivue 
            - ipyniivue : https://github.com/niivue/ipyniivue
                - eliz finds this is slow on binder ? is it a memory requirement ?
            - https://niivue.github.io/niivue/features/alphathreshold.html
            - Currently in use in FSL docs : https://git.fmrib.ox.ac.uk/fsl
    - Suggested actions items
        - Work with NiiVue on Python API
        - Where can Nilearn functionality be replaced by NiiVue
    - Could start it as a satellite project that can be later merged
    - Start with generating examples with what NiiVue can do that's not possible in Nilearn
    - NiiVue API: https://niivue.github.io/niivue/devdocs/Niivue.html

**Not discussed because of lack of time, send email about these:**
- Release schedule
- Office hours
    - Suggestion to change name to "drop-in hour"
    - Change day?

##### Open issues and PRs

- Failures in [nilearn/decomposition/tests/test_canica.py](https://github.com/nilearn/nilearn/issues/3441)
    - https://github.com/nilearn/nilearn/actions/runs/3687387852/jobs/6240911647
    - https://github.com/nilearn/nilearn/actions/runs/3687387852/jobs/6240912168

## November 22nd 2022

**Attending:**

- Elizabeth
- ~~Nicolas~~
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- Taylor

### Agenda

##### General

- Core dev meeting time
    - Keeping at the current time
    - Please let Yasmin know if you can't make it ; will reschedule if not enough people can attend a given call
- Meeting with Kshitij Chawla about automatic formatting 
    - See https://github.com/nilearn/nilearn/issues/2528
    - Current plan is that Kshitij will implement it in a PR and then assess relative impact
- Discussion with Jérôme about surface data support
    - See proposal: https://github.com/nilearn/nilearn_sandbox/tree/master/discussions/surface_api_office_hours_2022-10-14
    - Everyone take a look at the proposal and give feedback before moving forward
    - Jérôme will make updates to integrate notes from last office hours discussion
    - After everyone agrees with the plan, set up a meeting with Chris to share our proposal
- Updates about issues/PRs for release
    - https://github.com/nilearn/nilearn/pull/3173 could use another review
    - https://github.com/nilearn/nilearn/issues/3171 <-- needs a PR ?
        - Opened an issue on FreeSurfer : https://github.com/freesurfer/freesurfer/issues/1033
    - Safe cache : https://github.com/nilearn/nilearn/pull/3375
        - Decision to remove the function
    - HTW needs to finish #3204 (accept index-like input for load_confounds sample mask)
- Do release first week of December
- Python 3.6 support
    - Plan to extend deprecation cycle to 0.11 release

##### Open issues and PRs

- [CI migration](https://github.com/nilearn/nilearn/pull/3383)
    - Finished and open to being reviewed
- [User guide](https://github.com/nilearn/nilearn/issues/3379)
    - Discuss during next office hours (25/11, 2/12)
    - Will not include as a milestone in next release
- Performance of maskers
    - Take first steps to better document behavior
    - Plan an office hour discussion around this
    - Some relevant issues:
        - https://github.com/nilearn/nilearn/issues/3413
        - https://github.com/nilearn/nilearn/issues/3398
        - https://github.com/nilearn/nilearn/issues/3399
        - https://github.com/nilearn/nilearn/issues/3177

## October 11th 2022

**Attending:**

- Elizabeth
- Nicolas (I will be in the train. I'll try to connect on my phone...)
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- Taylor
- JB

### Agenda

##### General

- CZI position
    - Already had one interview
    - Start sending out posting through various channels this week
        - See draft: overleaf.com/3674263154gyndmhhjpngh
- Issues with Neurostars platform
    - We don't have a template. This is a feature supported by Discourse, but not actually used in Neurostars.
    - Can't monitor posts. Neurostars doesn't have any admins moderating posts (e.g., asking folks to open a new topic when their topic has meandered away from the original question).
    - There will be costs to switching platforms, so will focus on improving Neurostars first.
    - ACTION ITEM: Will reach out to INCF about our concerns and requests
- Office hours format
    - Adding a monthly meeting for Asia Pacific time zone
        - Send email to figure out a date and time
        - Do more extensive advertising beforehand
    - Having an agenda - limit to one item for discussion
    - Renaming "office hours" to "drop-in hours"?
        - https://twitter.com/LaurenSHallion/status/1562474858759327746?s=20&t=L8Y6hGjOgVfRpN5QvOC3mA
        - Revisit after having a break from the office hours
- Milestones for 0.10.0 release
    - https://github.com/nilearn/nilearn/milestone/21

##### Open issues and PRs

- [CI service discussion #3239](https://github.com/nilearn/nilearn/issues/3239)
    - Decision to migrate CI to github actions
- [Some tests fail in test_nilearn_standardize on aarch64 and ppc64le #3363](https://github.com/nilearn/nilearn/issues/3363) (particularly if we want to support testing other architectures)
    - Decision: Improve test for failure in issue; For now don't add support for other architectures
- [Reorganizing the User Guide #3379](https://github.com/nilearn/nilearn/issues/3379)
    - Focus on changes in macroscale
- [Latex error for rendering equations #3381](https://github.com/nilearn/nilearn/issues/3381)


## September 20th 2022

**Attending:**

- Elizabeth
- Nicolas
- Bertrand
- Jérôme
- Alexis
- Hao-Ting
- Yasmin
- Taylor (has to leave 15 mins early)
- JB

### Agenda

##### General

- CZI application accepted
    - Ideally constrain position to Montreal but can consider other options (consulting)
    - Make a posting to push through our networks
        - Edit community-oriented posting here : https://www.overleaf.com/3674263154gyndmhhjpngh
        - First pass at places to advertise the posting : 
            - https://github.com/nilearn/dev-days-2020/issues/9
            - https://github.com/nilearn/dev-days-2021/issues/5
    - Update previous McGill Seb position
        - Relevant information from Seb for creating posting for McGill :
            > the McGill position has to match the applicant experience pretty closely, hiring an applicant on a specific profile has to be justified and approved by admin (who I don't know). If you are looking for some "super interesting" reading, check this out: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjvjJH04qP6[…]job_catalog_june_2021_3.xlsx&usg=AOvVaw3wWzitEgmQnX7CU_a5ridT
            >
            > the roles we were told would fit for our original call (pretty senior dev) were, in order of seniority:
              - IST2R
              - IST3S
              - IST3R
- Major release and setting milestones
    - Yasmin will start setting milestones
- New documentation theme
    - Dev/stable banner is gone
        - Look into making a way to toggle between two (open an issue)
    - News section is gone, do we want it back?
        - Update maintenance doc to take out news sections update instructions
    - Update what's new to changelog? Decision: no, keep the same
- Reorganizing website (see [comment](https://github.com/nilearn/nilearn/pull/3125#issuecomment-1196040759))
    - Think about our audience
        - CS or neuro background (or both)
    - Restructuring user guide
        - Reodering topics so order is more logical (start here)
    - Cleaning and organization of examples
        - e.g. see discussion in issue [2283](https://github.com/nilearn/nilearn/issues/2283) about deprecating some fetchers
        - Can we get analytics data on examples? (Yasmin)
            - Alexis suggested https://matomo.org/pricing/?menu
    - Which topics/sections should be prominent and which can be buried or removed
    - See if we can get inspiration from https://psy3018.github.io/cartes_cerebrales.html (eliz : but try to be careful about keeping content in scope)
- Discussion with Chris about surface data support
    - See [Coordinate Image API](https://nipy.org/nibabel/devel/biaps/biap_0009.html)
    - Also nibabel PR [#1090](https://github.com/nipy/nibabel/pull/1090)
    - This will take a long time to finish, shall we move on with our own implementation?
    - Jerome: If we want to move forward with nilearn Surface object implementation we need to rethink its structure
    - Plan a brainstorm session to discuss further
- Alexis: possibility of plotting several contrast maps on a surface (open an issue)
- Issues with Neurostars platform [--> Move to next month]
- Office hours format [--> Move to next month]
    - Adding a monthly meeting for Asia Pacific time zone
    - Having an agenda

##### Open issues and PRs

- https://github.com/nilearn/nilearn/issues/2528
- https://github.com/nilearn/nilearn/pull/2682

## June 7th 2022

**Attending:**

- Elizabeth
- Nicolas
- Bertrand
- Jérôme (leaving at 30 mins)
- ~~Gael~~
- Alexis (will not be able to join)
- Hao-Ting
- Yasmin
- Taylor

### Agenda

##### General

- CZI application submitted!
- Updates on Brainhack OHBM’22
    - Nilearn project submission
    - Nilearn talk: put the talk on GitHub so everyone can review it!
- CircleCI plan
    - Are we happy with this? Keep?
    - Any news on open-source version?
    - See #[3239](https://github.com/nilearn/nilearn/issues/3239)
- Cleanup of `Nilearn.github.io` - Nicolas will delete older folders in root
    - Relating to comment of Nicolas in [#3270](https://github.com/nilearn/nilearn/issues/3270)
    - Search functionality on our github pages
        - Google search does not lead to stable pages
- EuroSciPy 2022 (Monday, August 29 to Friday, September 2 in Basel)
    - Suggestion to submit proposal to present Nilearn
    - Ask Raphael if he's interested (Yasmin)
- Nilearn office hours summer break
    - This Friday: announcing for Brainhack
    - Break from next week, restart in September
    - Rethink the format
        - Theme
        - Monthly townhall?
        - Look at other projects (e.g., MNE-Python)
        - Request feedback at BrainHack / OHBM

##### Open issues and PRs

- Update surface functions [#2682](https://github.com/nilearn/nilearn/issues/2682) Should we wait for nibabel's SurfaceImage to be implemented ? Coordinate with nibabel team.
    - Approach nibabel team at OHBM
    - nibabel office hours (there's a session available this week, see [nipy discourse](https://nipy.discourse.group/t/announcement-nibabel-office-hours/118))
- Adding a Code of Conduct [#3264](https://github.com/nilearn/nilearn/issues/3264)
    - Combine nipy and contributor covenant?
    - open a PR with contributor covenant
- PR [2725](https://github.com/nilearn/nilearn/pull/2725) - consistent 1D inputs for `inverse_transform`
    - James identified the maskers that might return 3D outputs at the moment: https://github.com/nilearn/nilearn/issues/2726#issuecomment-794575338
    - We should review the maskers' inverse_transform and GLM outputs to see what produces 4D vs. 3D. Open an issue about it.
    - Consensus is that it would be reasonable to return 3D outputs when it is clear that there is no sample dimension (though there are probably backwards-incompatibility issues to deal with).

## May 10th 2022

**Attending:**

- Elizabeth
- ~~Nicolas~~ (en formation)
- Bertrand
- ~~Jérôme~~
- Gael
- ~~Alexis~~
- Hao-Ting
- Yasmin
- Taylor
- JB

### Agenda

##### General
- CZI grant:
    - [To-do list and material needed for this round](https://github.com/nilearn/Applications/tree/main/2022-CZI-EOSS-Cycle-5)
    - who is the grant's PI ?
    - what do we need in terms of official (University) support ?
    - ~~Need letters from other partners projects (fitlins, MNE, ...) ?~~
- CircleCI:
    - we have bought a plan (currently working)
    - after discussing th CircleCI people there seems to be a free OSS plan (tbc)
    - opened issue [#3239](https://github.com/nilearn/nilearn/issues/3239)
- updates on Brainhack OHBM'22 
    - Hao-ting, Elizabeth attending in person, Bertrand virtually, Taylor (probably) virtually
    - Prepare labels for issues related to Brainhack (Hao-Ting can help Yasmin with this)

#### Open Issues and PRs

-  Setting up nilearn development environment per instructions fails as tbb is not installed [#3244](https://github.com/nilearn/nilearn/issues/3244) 
    -  Taylor: I think this is `mkl`'s fault, and I was unable to reproduce with `conda`, so it could be homebrew-specific as well. Do we even need `mkl`? It's a docs-specific requirement, and I don't know where it's used.
    -  Gael: Remove mkl dependency.
-  Issues when using matplotlib version 3.5.1 [#3236](https://github.com/nilearn/nilearn/issues/3236)
    -  Yasmin could not reproduce issue
    -  Will give another nudge to contributer to reproduce on public data 
- `0.9.1` tests fail with 4 `Assertion Errors` in `interfaces/fmriprep/tests/test_load_confounds.py` [#3232](https://github.com/nilearn/nilearn/issues/3232)
    - Hao-Ting: Rounding error? How to proceed with this kind of bug
        - Increase the length of the simulated signal
        - Investigate the collinearality of the confounds
- GLM+TFCE PR [#3196](https://github.com/nilearn/nilearn/pull/3196) may need one more review.

## April 5th 2022

**Attending:**

- Elizabeth (will also leave 15m early)
- Nicolas
- Bertrand
- Jérôme
- Gael
- Alexis
- Hao-Ting
- Yasmin
- Taylor (have to leave 15 min early)

### Agenda

##### General

- Time set-up for office hours (UTC time or ... ?)
    - [Nipy calendar](https://calendar.google.com/calendar/u/0?cid=ZjJwM3E5NWs1aHBiaHBpaTQ5czJoZWFpY3NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)
- CircleCI now has a 1h limit of build time for its free plan which means that all full build are currently canceled in our CI pipelines. (@Nicolas)
    - Bertrand : I can take the point
- Nilearn job posting / CZI
- Patch release 0.9.1 (@Nicolas)
    - What is still missing?
    - Due date?
    - decision: merge 3098 and do 3158, then release
- New documentation theme PR [#3125](https://github.com/nilearn/nilearn/pull/3125)
    - need to proof read User Guide
    - should be able to deploy next time we meet
- Background images PR [#3173](https://github.com/nilearn/nilearn/pull/3173)
    - integrate changes for `view_*()` methods in different PR for easier reviewing
- Brainhack 2022 / OHBM Glasgow: any more info ?
    - [Brainhack landing page](https://ohbm.github.io/hackathon2022/)
- [name=Gael] Me stepping down officially?
    - After a few farewell drinks at OHBM

## March 8th 2022

**Attending:**

- Elizabeth
- Nicolas
- Bertrand
- ~~Thomas~~
- Jérôme
- ~~Gael~~
- Alexis
- Hao-Ting (have to leave 10 minutes early)
- Taylor (have to leave 15 min early)

### Agenda

##### General

- News from the engineer job posting? (Bertrand)
    - Currently hiring: Yasmin Mzayek ; might arrive on April 1st
- Montreal job posting: JB will write posting
    - Jérôme and Elizabeth will edit the [existing posting](https://github.com/nilearn/admin/tree/main/proposals/engineer_2022) as a first pass
    - New overleaf document available here : https://www.overleaf.com/3674263154gyndmhhjpngh
    - updates ? Not yet ready, we will update ASAP and circulate 
- Parietal (B.Thirion and A.Gramfort) got a small grant with people at Montreal (P.Bellec and K.Jerbi) to pay for travel and collaborations
    - mostly dedicated to software aspects: Nilearn and MNE
    - most actions targeted in 2022: brain hack at OHBM 2022 and Main conference in October
- Updates on OHBM brainhack ? (16-18 June)

#### Open Issues and PRs

- [#3167](https://github.com/nilearn/nilearn/issues/3167) 64-bit integer NIfTI images
    - Will require identifying where Nilearn writes out images and update to avoid creating int64. Wide (if not difficult) changes
- [#3158](https://github.com/nilearn/nilearn/issues/3158) Add note for new maskers module in examples
- [#3173](https://github.com/nilearn/nilearn/issues/3173) Allow not scaling background maps for surface plots (PR by A.Thual)
    - Still looking to add [flat maps](https://github.com/tknapen/tknapen.github.io/wiki/Pycortex-flattening) for different fsaverage resolutions. Alexis will contact Alex Huth to see whether he can provide existing maps
    - Open question as to how to update the API to better accomodate new parameters -- input welcome !
- [#3172](https://github.com/nilearn/nilearn/issues/3172) [ENH] Radiological view for cross-sectional MRI plotting
    - Provide guidance for new contributor as needed
- [#3122](https://github.com/nilearn/nilearn/issues/3122): Refactor documentation's theme
    - Changes to Sphinx-Gallery now merged (:tada:) to allow for hierarchical structure
    - Developers can divide docs to run through individual categories
    - Alexis will generate a live preview and then it can be divided among the developers, with Alexis' guidance on what should be evaluated
    - Could be good to have Yasmin's review on the doc structure as part of orienting to the library
- [#3085](https://github.com/nilearn/nilearn/issues/3085): correspondence between atlas region labels and NiftiLabelsMasker's output dimensions
    - Allow use of dictionary for labels. Deprecate use of list, but make the deprecation cycle very long since atlases use lists and users are used to lists.
    - Update atlases to have new dictionary label attribute. Don't replace the old one, just add a new one.
- [#3160](https://github.com/nilearn/nilearn/issues/3160)
    - Could merit a sooner patch release

#### Other points

- Bertrand: have been missing a few open hours recently, but should be back in March !



## February 7th 2022

**Attending:**

- Elizabeth
- Nicolas (I'll try to join, will have to leave at 17h30 max)
- Bertrand
- ~~Thomas~~
- Jérôme
- ~~Gael~~
- ~~Alexis~~
- Hao-Ting
- Taylor

### Agenda

##### General

- News from the engineer job posting? (Bertrand)
    - One good candidate: Yasmin Mzayek ; itw by Nicolas pending ; might arrive on April 1st 
        - Background in neuroimaging + experience with some softwares and standards (FSL, ANTS, BIDS...)
        - Some experience with machine / deep learning
        - Some experience with Python, Git/Github but mostly scripting
        - Less experience in software engineering in general
        - No experience in CI/CD, documentation with Sphinx
        - Overall feeling: Good candidate who should be able to learn the missing competences
- Montreal job posting: JB will write posting
    - Jérôme and Elizabeth will edit the [existing posting](https://github.com/nilearn/admin/tree/main/proposals/engineer_2022) as a first pass
    - New overleaf document available here : https://www.overleaf.com/3674263154gyndmhhjpngh
- Organization for next meetings and office hours?
    - Nicolas: availability ?
        - Current time for office hours should work most of the times plus/minus a conflict from time to time
        - Current time for core-dev meetings works very poorly for me. Tuesday same time would be better
            - Update to Tuesday 6pm CET moving forward
    - Should someone else organize these? (Bertrand for the time being)
- hackathon in 2022 ? Coupled with OHBM ? Brainhack ? Any better suggestion ?
- OHBM Brainhack (16-18 June) will be hybrid, Nilearn would be a good project to submit with well-curated issues for beginners
- *Not* hold a Nilearn Dev Days this year and instead focus on the BrainHack
- Currently applying for funding for an in-person event in autumn in Montreal
    - Aim to have a Montreal-based developer before the event

#### Open Issues

- [#3132](https://github.com/nilearn/nilearn/issues/3132) :  Inconsistent behaviour of inverse_transform() in masker classes
    - Revive stale PR
- [#3122](https://github.com/nilearn/nilearn/issues/3122): Refactor documentation's theme
    - Pick up with Alexis directly
- [#3085](https://github.com/nilearn/nilearn/issues/3085): correspondance between atlas region labels and NiftiLabelsMasker's output dimensions
    - Allow use of dictionary for labels. Deprecate use of list, but make the deprecation cycle very long since atlases use lists and users are used to lists.
    - Update atlases to have new dictionary label attribute. Don't replace the old one, just add a new one.
- [#3058](https://github.com/nilearn/nilearn/issues/3058): Passing a 4D image to SecondLevelModel 
- [#3120](https://github.com/nilearn/nilearn/issues/3120): view_img always masks bg_img with MNI mask
    - threshold only when using Nilearn default option; never threshold image when user-provided

#### Other points

- Jupyter book of advanced analyses?
    - Too much work for nilearn team, but maybe link to workshops/tutorials that use nilearn in documentation.
        - Would be useful to have this list even internally to create metrics for e.g. funding applications in the future
        - List of tutorials should document which versions of Nilearn they run under (and e.g. date of workshop)
    - More general question of how to handle compute-heavy examples
        - Could pitch developing these examples as a hackathon project ?


## January 10th 2022

**Attending:**

- ~~Elizabeth~~
- Nicolas
- Bertrand
- ~~Thomas~~
- Jérôme
- ~~Gael~~
- Alexis
- Hao-Ting
- Taylor

### Agenda

##### General

- News from the engineer job posting? (Bertrand)
    - Candidates? Scheduled interviews?
- Montreal job posting: JB will write posting
- Organization for next meetings and office hours?
    - Nicolas: I still don't know if I'll be available at the current times (Fridays and 1st Mondays of each month)
    - Should someone else organize these?

##### Documentation

- Question from Taylor: Would it be reasonable to include modeling examples in the docs that involve fairly common analyses, but more custom code? I'm specifically thinking of:
  - Task-based functional connectivity with beta series (LSA, LSS) and psychophysiological interactions (PPI).
  - A FIR example focused on HRF estimation instead of localization, perhaps combined with custom HRF use. Preferably this would involve both FIR and standard HRFs in the same design matrix, for different conditions.
    - Look at recent Kay paper on naturalistic dataset with custom HRF modeling. (space-varying HRF?). https://www.nature.com/articles/s41593-021-00962-x.
    - Given how finicky this analysis is, maybe just link to other package that does this.
  - Modeling with parametric modulation vs. duration modulation.
      - Look at reaction time in existing datasets.
  - Incorporating temporal and dispersion derivatives into results, as in [Calhoun et al. (2004)](https://doi.org/10.1016/j.neuroimage.2003.12.029).
      - BT: Need to check.
  - An alternative might be to have some of these methods in a separate repo, housed in a Jupyter book.
    - BT: Some of these examples (eg FIR) seem within-scope.
    - HTW: Need to look into datasets that would work for PPI.
- New documentation theme (Alexis)
    - We had a small demo last Friday for the office hour
- Re-organize the landing page?

##### Current issues

- Deprecation of some fetchers
    - See issue https://github.com/nilearn/nilearn/issues/3086
- Move BIDS- and FSL-related functions from `_utils` to `interfaces` module
    - See issue https://github.com/nilearn/nilearn/issues/3118
- Sphinx-tabs extension
    - See issue https://github.com/nilearn/nilearn/issues/3107
- warn instead of raising error when affines differ (math_img): https://github.com/nilearn/nilearn/issues/3115


##### Release 0.9.0

- **Goal:** Make the release before the **end of January** (ideally before the very end such as to have someone full time on potential bugs and issues...)
- See milestone: https://github.com/nilearn/nilearn/milestone/19
- Replace numpy with pandas in data loaders (https://github.com/nilearn/nilearn/pull/2829)
    - Nicolas: Goal is not clear, are we trying to get rid of rec arrays in favor of pandas dataframes?
    - What about arrays? lists?
- New maskers module (https://github.com/nilearn/nilearn/pull/3065)
    - 3 approvals so far (bertrand, Jerome, and Taylor).
    - Should we have another core-dev reviewing it?
- Include Hierarchical KMeans in regions.Parcellations (https://github.com/nilearn/nilearn/pull/2282)
    - Thomas, do you know if you'll have the time to answer Jerome's review?
    - If not, I think we should merge as remaining points were minor
- Refactor plot_matrix (https://github.com/nilearn/nilearn/pull/3001)
    - It'd be nice to have another review

##### Current PRs (not in 0.9.0 milestone)

- avoid unnecessary data loading if dtype casting not needed: https://github.com/nilearn/nilearn/pull/3114


## December 6th 2021

**Attending:**

- Elizabeth
- Nicolas
- Bertrand -> will arrive late, ca 5:30 CET, sorry !
- ~~Thomas~~
- Jérôme
- Gael
- Alexis (NeuroSpin retreat)
- Hao-Ting
- Taylor

### Agenda

- Next meeting on January 3rd or 10th? (since people might still be on holidays on the 3rd...)
    - postpone it to week after

- Current issues
    - General atlas fetcher and templateflow: https://github.com/nilearn/nilearn/issues/3074
        - Actions on the Nilearn's side: https://github.com/nilearn/nilearn/issues/3075
        - Add a pointer to templateflow
        - Explain that nilearn's scope is not to provide a general data fetcher, they should only be used for examples
        - Remove from docs that we welcome atlases
        - I think we agree on this one but in case someone wants to say something...

- Current PRs
    - Include Hierarchical KMeans in regions.Parcellations: https://github.com/nilearn/nilearn/pull/2282
        - @thomas do you have the time to answer's Jerome's review? (Otherwise I think we should rebase and merge)
        - answer :+1: will take those into account soon.
    - Add displays to API: https://github.com/nilearn/nilearn/pull/3073
        - Needs some reviews
    - New maskers module: https://github.com/nilearn/nilearn/pull/3065
        - Also needs some reviews

- Next release :tada: 
    - Around December 15th or should we wait for early January?
        - "New year, new nilearn"
    - 0.8.2 or 0.9.0?
    - Highlight plotly plots
    - I think we have a lot of changes since 0.8.1 (new modules, new plotting capabilities, new functionalities), so it could be worth bumping to 0.9

- Doctoral mission of Raphael Meudec
    - We suggested with Bertrand that he works on improving BIDS support of Nilearn
    - Any other ideas/suggestions?
    - Improving surface plotting capabilities (add contours - especially for plotly, connectome)
    - GLM reports design matrices shapes
    - GLM reports interactivity
    - drawing contours of regions with plotly

- Development
    - Should we add a roadmap page to the docs?
        - https://nipy.org/nibabel/devel/roadmap.html
        - https://scikit-learn.org/stable/roadmap.html
    - Go further with development proposals?
        - ex: https://nipy.org/nibabel/devel/biaps/biap_0000.html
        - Nilearn Development Proposals (NDPs) or something alike?

Bonus if time allows:

- Engineer job description for Nilearn
    - Add latex sources to the Nilearn admin repo
    - Add scenarios for the position?

---

## November 8th 2021

**Attending:**
- Elizabeth
- Nicolas
- Bertrand
- Thomas
- Jérôme
- Gael
- Alexis
- Hao-Ting

**Apologies:**
- Taylor

### Agenda

- New team member
    - Welcome Hao-Ting! :tada: 

- Office hours
    - Time used to be 4pm-5pm UTC every Monday, which used to be 6pm-7pm Paris time, but is now 5pm-6pm due to winter time.
        - This will overlap with future core-dev meetings
    - Current time is not great for everyone, should we change?
    - New time: Friday 4pm UTC

- Feature requests
    - use [ancpbids](https://github.com/ANCPLabOldenburg/ancp-bids) to handle BIDS datasets: See issue [#3045](https://github.com/nilearn/nilearn/issues/3045) and PR [#3044](https://github.com/nilearn/nilearn/pull/3044)
        - package is quite new (created this summer)
        - no docs so unsure what it's doing...
        - no coverage information...
        - I basically said "no" in a polite way, but the person keeps sending me messages on discord about this, so asking the team opinion such that I can close (or not?) this for good.
        - Would apreciate some feedback from BIDS-knowledgable team member (Taylor ?)
        - He/She might join the following office hour to talk about this
        - **Taylor**: Erdal has been looking into using more established schema tools for the BIDS specification than what we currently use (which is just an _ad hoc_ YAML "standard" based on the actual JSON schema). He's also working on querying/file-generating tools for BIDS, as a sort of replacement for pybids, with the hope that the pybids team will adopt it. The combination of these two efforts is ancp-bids. I think he's a little frustrated with the lack of response from the BIDS spec and pybids teams, since his proposal for pybids would basically rebuild it from scratch and his proposal for the spec would involve adopting schema tools that not many folks have experience with. I think ancp-bids might be useable, but I worry about long-term support after he finishes his degree. I can try to take another look soon-ish to see what state ancp-bids is in and to determine if a reduced-dependency version might be workable?
        - Short term: help developing the package and see how it goes
        - Needs tests and docs at least

- Current issues
    - No burning issues I believe, please add if you feel like we should discuss something in particular.


- Current PRs
    - Include Hierarchical KMeans in regions.Parcellations: https://github.com/nilearn/nilearn/pull/2282
        - Seems to be ready for merging
        - bertrand for one last look
    - Refactor change logs: https://github.com/nilearn/nilearn/pull/3049
    - Plotly and Matplotlib surface figures: https://github.com/nilearn/nilearn/pull/3036
        - remove init_with_figure
        - comments on docs
    - NiftiMapsMasker Reporting: https://github.com/nilearn/nilearn/pull/2880
        - Check that figures are not created all at the same time

- ``input_data`` module discussion
    - We spent a lot of time discussing this last meeting and decided to take a month to think about it.
        - As a refresher, you can read the cleaned notes [here](https://github.com/nilearn/admin/blob/main/meeting_notes/04_10_2021.rst)
        - Move all ``load_confounds`` utilities to ``interfaces.fmriprep``
        - Taylor opened issue [#3014](https://github.com/nilearn/nilearn/issues/3014) to collect user feedbacks
    - It's important to decide where we want to put the ``load_confounds`` utilities (currently in ``input_data``) before the next release as to avoid an unecessary deprecation cycle...

- Plotting API, displays
    - The objects from [displays.py](https://github.com/nilearn/nilearn/blob/main/nilearn/plotting/displays.py) look like they are public but only the ``OrthoSlicer`` appear in the [API docs](https://nilearn.github.io/stable/modules/reference.html#module-nilearn.plotting)
    - This, combined with the lack of documentation, might be a reason why users have issues interacting with nilearn plots
    - Proposal:
        - Turn displays into a folder
        - Seperate slicers, projectors, and brand new surface figures in different files
        - Add relevant objects to the API docs
        - Add a section somewhere in the user guide and/or modify some examples to showcase how to customize plots with these.

Less important points not discussed during last meeting:

- Development
    - Should we add a roadmap page to the docs?
        - https://nipy.org/nibabel/devel/roadmap.html
        - https://scikit-learn.org/stable/roadmap.html
    - Go further with development proposals?
        - ex: https://nipy.org/nibabel/devel/biaps/biap_0000.html
        - Nilearn Development Proposals (NDPs) or something alike?

- Surfaces
    - Lots of recent feature requests (mostly extending the capabilities of the `image` module to surfaces)
    - Do we have a vision/scope for what Nilearn should be able to do with surfaces? A roadmap? Should we clarify these points in the docs?
    - News on surface representation from Nibabel:
        - Recent meeting (Chris, Eric, Hao, Nicolas, Matthew)
        - https://hackmd.io/ZXcVpr1wQvmQIq9Sl1Vidg
        - https://github.com/nipy/nibabel/pull/1056
        - https://nipy.discourse.group/c/surface-api/10 


---

## October 4th 2021

**Attending:**
- Elizabeth
- Taylor
- Nicolas
- Bertrand
- Thomas
- Jérôme
- ~~Gaël~~
- Alexis

### Agenda

- New team member(s)
    - Core devs
        - Welcome Alexis!
        - Propose to Hao ? (Bertrand, Nicolas?)
            - Already done!
        - Other ideas?
            - No
    - Triage
        - Ideas for new members?
            - Add a few lines in contributing docs for defining what the triage team would be responsible to.
            - Other kind of contributions (answers questions on neurostars, issues...)
            - Post a message on discord and allow people to self nominate

- Changing the name of the module `input_data`
    - Should we do it?
    - Deprecation cycle length?
        - Alias maskers in old module while moving? This would allow a long deprecation cycle.
    - Names? (`io`, `bids`...)
        - io not so great because too large scope
        - Possibly move maskers into `masking` _or_ move `apply_mask`/`unmask` to wherever maskers end up.
    - Have a look at `_utils` and see if we should make some utilities public
    - Why are NiftiMaskers called *nifti* (Daniel Gomez's issue): [#2844](https://github.com/nilearn/nilearn/issues/2844)
    - If SurfaceMaskers and VolumeMaskers will share the same kind of API, it'd make sense to have them all in a masker module.
    - `interfaces` module? And then `fmriprep`, `bids` would be submodules
    - Make the discussion public ==> open issue

- Pull Requests needing reviews
    - [INFRA] Add dev docs deployment job [#2968](https://github.com/nilearn/nilearn/pull/2968)
    - [NF] migrate package load_confounds main function load_confounds [#2946](https://github.com/nilearn/nilearn/pull/2946)
    - [ENH] Add Plotly support for surface plotting [#2902](https://github.com/nilearn/nilearn/pull/2902)

- Issues needing discussion
    - No burning issues needing discussion here AFAICT (feel free to add some if I missed something)

- Development
    - Should we add a roadmap page to the docs?
        - https://nipy.org/nibabel/devel/roadmap.html
        - https://scikit-learn.org/stable/roadmap.html
    - Go further with development proposals?
        - ex: https://nipy.org/nibabel/devel/biaps/biap_0000.html
        - Nilearn Development Proposals (NDPs) or something alike?

- Surfaces
    - Lots of recent feature requests (mostly extending the capabilities of the `image` module to surfaces)
    - Do we have a vision/scope for what Nilearn should be able to do with surfaces? A roadmap? Should we clarify these points in the docs?
    - News on surface representation from Nibabel:
        - Recent meeting (Chris, Eric, Hao, Nicolas, Matthew)
        - https://hackmd.io/ZXcVpr1wQvmQIq9Sl1Vidg
        - https://github.com/nipy/nibabel/pull/1056
        - https://nipy.discourse.group/c/surface-api/10 

    - Add message in surface issue for next meeting

Next meeting: November 8th 16h - 17h (Paris time).

---

## September 6th 2021

**Attending:**

_Note: Monday is labor day in the US and Canada_

- ~~Elizabeth~~ (Hollidays)
- ~~Taylor~~ (hollidays)
- Nicolas
- Bertrand
- Thomas
- ~~Jerome~~ (Hollidays)
- Gael

### Agenda

- Feature requests
    - Smoothing function for surface based data (see this Neurostars post https://neurostars.org/t/smoothing-surface-data/20159).
    - Also related: https://github.com/nilearn/nilearn/issues/2747

--> TODO: Nicolas open issue and explain problems and ideas (take neighborhood using edge weights)

- Current PRs
    - Plotly PR is quite large and would benefit from more reviews: https://github.com/nilearn/nilearn/pull/2902
    --> ask jerome to ask sebastien urch for plotly help
    - Contributing docs PR had some recent activity. Anything we can do here Thomas? https://github.com/nilearn/nilearn/pull/2755

- Next release (0.8.1)
    - Aiming for mid-september (before team retreat would be cool)
    - Created a milestone for it
    - Any PR and/or issue that need to be addressed?

- Feedback on Office hours
    - had 3 events so far but relatively little interest (2 persons for first one, and one person for last one)
    - are there things to improve communication wise?
    - Leave message on general channel giving the next office hours

- Projects for the team retreat around Nilearn
    - Alexis proposed to tackle the website design
    - Other ideas?
        - Stephanie Noble can provide useful feedback

- Team members
    - I think Elizabeth mentioned last meeting that we should renew some of the core-dev team since thomas and elizabteh will defend soon (right?)
        - Some ideas: Alexis Thual (+1 for bumping Alexis up), Raphael Meudec
        - Hao Ting
        - Sage Hahn opened a interesting PR last year, maybe too late https://github.com/nilearn/nilearn/pulls/sahahn
        - Other team than coerdevs ? web, docs, etc

---

## July 5th 2021

**Attending:**
- Elizabeth
- Taylor
- Nicolas
- Bertrand
- Thomas
- Jerome
- Gael

### Agenda

- Current issues
    - Correlation-base MVPA follow-up after last office hours (https://github.com/nilearn/nilearn/issues/2742)
        - BrainIAK RSA : https://brainiak.org/tutorials/06-rsa/
        - TODO : Close issue
        - Optionally follow up with BrainIAK and/or PyRSA teams about aligning their approaches with nilearn more.
    - Decoder cross-validation issue https://github.com/nilearn/nilearn/issues/2883, https://github.com/nilearn/nilearn/issues/2886
      - Advise users not to perform parameter selection/grid search with imaging data? Low statistical power, parameter selection is noisy process with high chance of overfitting. Do model averaging.
      - Make sure that the thing runs using a GridSearchCV classifier
      - Fix example and documentation so it's clear that there is no nested CV implemented/possible within Decoder.

- Current PRs
    - Contributing docs PR https://github.com/nilearn/nilearn/pull/2755 (stalled, can we help you @thomas?)
        - Please check out the recent build artifacts to see the issue with table rendering.
    - Deprecate surface functions API PR https://github.com/nilearn/nilearn/pull/2682 Should we merge?
        - Directly ask Chris whether nibabel is moving soon
    - Dev/Stable doc PR resurrected : https://github.com/nilearn/nilearn/pull/2605
        - round of reviews, then merge
    - Sphinx copybutton : https://github.com/nilearn/nilearn/pull/2838
        - Eliz confirmed that prompts (`>>>`) not copied with sphinx-copybutton

- Possible enhancements
    - Plotly for plotting https://github.com/nilearn/nilearn/issues/2793
        - green lights
    - Type hinting
        - GV: Don't discourage it, but don't force contributors to add type hints. Do it especially when it's not costly.
        - TS: Maybe look into sphinx extensions/settings to incorporate type hints into docstrings automatically.
        - TODO : Incorporate request for, but not enforcement of, type hints in contributing guidelines?
    - Follow-up on sprint discussions / suggested improvement
        - BIDS PR for GLMs: https://github.com/nilearn/nilearn/pull/2715
        - pybids-light library for searching BIDS datasets with minimal overhead: work hasn't really started, but we have "plans":
            - Repo : https://github.com/bids-standard/pybids-light
            - HackMD : https://hackmd.io/vlC0NvzmSYKkVVNUXnKlHQ
        - Surfaces: deprecation PR + check with Chris for better integration within Nibabel...
    - easier customization of nilearn plots: (i) adding references to useful objects (eg the colorbar axis) to the objects returned by nilearn plotting functions (eg BaseSlicer) (ii) adding an "advanced plotting" example. related: https://github.com/nilearn/nilearn/issues/2761
    - moving average pca? https://github.com/nilearn/nilearn/issues/2662
    - CircleCI artifacts : https://github.com/nilearn/nilearn/issues/2508

- Other
    - @NicolasGensollen in holidays (07 July - 18th July) ==> who can be there Monday 12th for the next office hours
        - change date : July 19th
    - Do we maintain them over the summer?
        - Skip
    - Do we maintain core-dev meeting August 2nd?
        - Skip
    - TODO: Onboarding new people in the team

---

## June 07, 2021
## Zoom Link : https://mcgill.zoom.us/j/87878325172

**Attending:**
- Elizabeth
- Taylor
- Nicolas
- Bertrand
- Thomas

**Apologies:**
- Jerome (out of town)
- Gael (unavailable)

### Agenda

- Tutorial materials from Montreal (@Gael @emdupre). :maple_leaf: 
    - TP around Nilearn at the end of June (@bthirion)
        - is https://github.com/illdopejake/RS2018_Nilearn_tutorial still usable ?
        - @gael: I use the tutorial examples at the beginning of the nilearn example pages
        - eliz NHA tutorial from last year : https://github.com/emdupre/nha2020-nilearn

- Sprint debrief :runner:
    - **Office hours**
        - Should we do it? Yes !
        - Who would be responsible? Whoever is available !
        - How often?
            - MNE holds every 2 weeks : https://mne.discourse.group/t/announcing-mne-python-office-hours/2468
        - What platform? Discord? +1 for Discord
        - Advertise every time on Twitter, neurostars...
        - Monday 6pm-7pm Paris time every two weeks (can vary time if needed)
        - Add them to Nilearn calendar: https://calendar.google.com/calendar/u/3/r?cid=bmlsZWFybi5ldmVudHNAZ21haWwuY29t
        - June 28th first date (advertise one week before)

    - **Website**
        - New post-sprint issue: https://github.com/nilearn/nilearn/issues/2824
        - Improve searching (get rid of google search)
        - Design/structure
        - Interactivity (write interactive demo next to binder buttons):
            - scikit learn example: https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html#sphx-glr-auto-examples-calibration-plot-calibration-multiclass-py
        - add office hours banner
        - remove sprint banner

    - **HTML reports**
        - Community wishes for more interactivity (browsing acrross subjects, interactive figures...)
        - Sould we merge https://github.com/nilearn/nilearn/pull/2707 ?
            - @gael: cursory look = looks great!
            - continue discussion on the issue (resampling at transform time)
        - @NicolasGensollen started working on a small side project around interactive GLMs with Dash

    - **BIDS integration**
        - Not really sure what was decided and what is the path forward
            - @tsalo: The biggest development was the plan to write a lightweight version of pybids that could be a dependency for nilearn.
            - @tsalo: We'll also continue working on functions to write out BIDS-like derivatives, as in https://github.com/nilearn/nilearn/pull/2715, but would be good to extend beyond GLMs.
            - @tsalo: Lastly, there was also talk about compiling benchmark datasets to be shared across projects (including pybids/BIDS-related tools).

    - **Surfaces**
        - Would be much easier if Nibabel could provide a format for us. Chris might be looking into this??
        - Should we merge https://github.com/nilearn/nilearn/pull/2682 ?
        - Plotly support

- credentials (OSF and others). :key: 
    - Nilearn account : https://osf.io/4r3jt/
    - Eliz to add as admin on development_fmri data set
    - Bertrand to add as admin on Nistats data sets
    - Who has them? 
        - @NicolasGensollen has them now!
    - Should we manage this better? (and other credentials...)
    - How is scikit-learn doing this ? (@Gael??)

- Rename master into main :hammer:
    - PR is ready: https://github.com/nilearn/nilearn/pull/2861
    - Should we go for it? When?
        - @gael : yes, now +++

- next release of Nilearn :tada: 
    - 0.7.2 or 0.8.0??
        - @gael: The list of new features is currently a bit light to call it a 0.8.0 IMHO
    - Would prefer to hit 0.8.0 (bye bye Python 3.5, hello f-strings...) drop it!! jump to 0.8
    - things that we should absolutely merge before? ~~load_confounds~~, fsaverage6 (https://github.com/nilearn/nilearn/pull/2815), surface deprecation (https://github.com/nilearn/nilearn/pull/2682), 
    - Don't wait on load_confounds for release
    - Nilearn project at OHBM hackathon ? https://github.com/ohbm/hackathon2021/issues
    - When?
        - Before OHBM
    - populate milestone 0.8

---

## May 03, 2021

**Attending:**
- Elizabeth
- Taylor
- Nicolas
- Jerome
- Gael
- Bertrand
- Thomas

### Agenda

- Set up a triaging team (Gael proposes)
    * Permissions: edit issues, close them, change their labels
    * Goals: help manage the issues
    * Potential positive side effect: on-board more external contributors
    * Team created as nilearn/triaging

- Rename "master" branch to "main" (everybody is doing it) after the sprint since Nibabel is still following master convention.
    - This GitHub guide is useful : https://github.com/github/renaming/tree/040636ea50e945875c70cc964d586f645e9bd810#renaming-existing-branches

- Sprint organization: touch base on what has been done:
    - communication (will send a last reminder on twitter and GitHub issue on Tuesday or Wednesday, others??) @NicolasGensollen
    - [website](https://nilearn.github.io/dev-days-2021/getting-started.html) has been updated over the weekend to make resources like Discord easier to find. Opinions?
    - Should we add the discord link in the [github issue](https://github.com/nilearn/nilearn/issues/2739)? (+: easy to find, - : might get some noise...) @NicolasGensollen
    - poll (do we have some results to talk about?)
    - How many registrants do we have so far? 115

- pbellec and team proposed to integrate load_confounds into nilearn (see [https://github.com/nilearn/nilearn/issues/2777](https://github.com/nilearn/nilearn/issues/2777)).
  Could be a good sprint item if we want to do it? Opinions?

- slides/Notebooks
    - they're here: [https://github.com/nilearn/dev-days-2021/tree/main/Notebooks](https://github.com/nilearn/dev-days-2021/tree/main/Notebooks)
    - we have content for intro/whatsnew, HTML reports, and Surface modeling. Opinions, thoughts on these?
    - agree on materials for other sessions:
        - Contributing crash course
          https://docs.google.com/presentation/d/1og9Ti4NG0wdUPabmGYfmgKiM2ysV2QLkv9hdwOxNg0A/edit?usp=sharing
        - Community feedback on website
        - BIDS
            - Draft of slides at https://docs.google.com/presentation/d/1_kGRtB6xIE167GgM2_dN-6Kr4Ft0Q_cPNYK_IqfALkk/edit?usp=sharing
        - Adoption : ask people to contribute to this kind of document, split participants in dedicated groups to think about a few promising improvements. https://hackmd.io/U1CMivSfQduTbCXjVlSG2g
        - Eliz: Pluses / Deltas is a nice framework here : https://www.lucidmeetings.com/glossary/plus-delta
    - Coordinate for presentations when multiple speakers

- TODOS
    - Put the link to the Notebooks somewhere and add explanations (clone and launch) such that folks can follow along (@NicolasGensollen)
    - Coordinate with Chris for the Nibabel whatsnew session (@NicolasGensollen)
    - Change Friday schedule: move adoption at 2 and add closing session at 5 (@NicolasGensollen)
    - other things?
    - populate google calendar @Bertrand
    - opening:
        - project vision : what goes in etc.
        - managing expectations
        - call for mutual help
        - how people can help
            - triage, review PRs, explain each other
        - find focus on one thing
        - [discord] voice  channel to ask for quick help
        - time organization
        - help channel
        - coffee break channel
        - hours
        - everything hapening on discord
    - core-dev channel
    - answer issue about correlation tool for MVPA [here](https://github.com/nilearn/nilearn/issues/2742) (@ThomasBazeille)

---
**Opening session**

* Nilearn vision:
Nilearn is an Open-source Python package for visualizing and analyzing human brain MRI data.
 
    * provides statistical and machine-learning tools for brain mapping, connectivity estimation and predictive modelling. 
    * brings  visualization tools  with instructive documentation & open community.
    * supports general linear model (GLM) based analysis 
    * leverages the scikit-learn Python toolbox for multivariate statistics with applications such as predictive modelling, classification, decoding, or connectivity analysis.
    * Joint sprint with Nibabel

    * Consequence: we can only add functionalities that we are going to maintain in the **long term.**
        * Quality matters: documentation, tests, examples etc. 
        * Need a choice / selection: what goes in, what does not
        * Discussion to make a choice (consensus)

    * Goal of this meeting
        * Better discover Nilearn and the ecosystem
        * Fix issues: new PRs
        * Open issues, suggest new features, issues with Nilearn as-is

* Practically, for this sprint
    * Everything will be on Discord + Github
        * Let people know when you tackle an issue (msg on Github)
    * use Discord rooms 
    * take breaks: coffee room channel
    * Limited Working hours: 3pm-8pm

* how to benefit from it
    * Team up, exchange, discuss on the Discord platform
    * identify issues that correspond to your level, aims, interests
    * Ask for help
    * there will be some discussion sessions: attend only if you are interested in this topic
    * danger: lose focus

* What is needed from you
    * Closing issues
    * review PRs
    * triaging team
    * communicate/explain

Thanks and enjoy ! 

---

## April 12, 2021

**Attending:**
- Elizabeth
- Taylor
- Nicolas
- Jerome
- Gael
- Bertrand
- Thomas

**Nilearn vision:**

Nilearn is an Open-source Python package for visualizing and analyzing human brain MRI data.
 
It provides statistical and machine-learning tools for brain mapping, connectivity estimation and predictive modelling. It brings  visualization tools  with instructive documentation & open community.
It supports general linear model (GLM) based analysis and leverages the scikit-learn Python toolbox for multivariate statistics with applications such as predictive modelling, classification, decoding, or connectivity analysis.


### Agenda
 
**Part 1 - Ongoing things in Nilearn:**
 
 - Handling datasets integrity with CircleCI ? (see PR [2752](https://github.com/nilearn/nilearn/pull/2752))
     - use simpler keys of the form `v1-datasetname`
 - Add correlation-based tool for MVPA ?? (see issue [2742](https://github.com/nilearn/nilearn/issues/2742))
     - we need to better explain the nilearn vision and draw a clear line between in-scope and outof-scope features.
 - Contribution doc (see PR [2755](https://github.com/nilearn/nilearn/pull/2755))
 - Vision? (Bertrand)
     - See above
     - prepare a longer version to help arguing about feature inclusion
 
**Part 2 - Coding sprint:**
 
 - remaining todos:

     - Communication
we took care of most of the items in the list (see [5](https://github.com/nilearn/dev-days-2021/issues/5)). Remaining items? Post a reminder in a couple weeks?
        - Send out email to registrants on the 26th
        - Send out a poll (on Twitter a week before the hack, in same reminder email to registrants) with questions about what areas folks want to contribute to and what areas they want to know more about.
            - Thomas will prepare the poll as a Google Form.
        - Eliz: Compile list of current sprint registrants from email s.t. we can contact them more directly with questions and also with reminders

     - People to contact directly?
Sent an email to Chris. Others?
        - Follow up with Chris about nibabel elements of hack.
        - & Matthew Brett
        - & Oscar Esteban

- Looking through current topics for sprint (https://nilearn.github.io/dev-days-2021/), we should prepare something and try to divide the topics among us
    - Taylor (& hopefully Chris): BIDS
    - Gael: contribution crash course
    - Gael: community feedback on nilearn website
    - Nicolas: HTML reports
    - Nicolas & Bertrand: what's new & introduction to the sprint
    - Jerome & Nicolas: Surface modeling
    - Thomas : Barriers to adoption
        - a few seed question / a predefined small canvas(+ and -) to kick-off discussion
- Update website to switch timing of reports, surface modelling sessions

- Come up with very easy good first issues.
I was thinking about small documentation ENHs like adding terms to the glossary or improving some references with bibtex... (other ideas?)

- Have a look at the current [project board](https://github.com/nilearn/nilearn/projects/6)
    - When reaching out to Nibabel, ask if we should add Nibabel issues to our existing project board or create a new Nibabel project board
 
 - next steps?
Prepare slides till Friday 30th
Add easy first issues: 50 people !

---

## March 1st, 2021

**Attending:**
- Elizabeth
- Taylor
- Nicolas
- Jerome
- Gael
- Bertrand
- Thomas


### Agenda
- Notepad failure
    - Do we have notes from last meeting? Need to add them to admin repo.
        - Bertrand: open a ticket to try and recover it
    - New pad URL?
        - Operating on HackMD for now, to revisit
- Vision (Bertrand) ?
    - Lost with Notepad crash: for next time ...
- Contribution PR template (Thomas) ?
    - Thomas to open draft PR with work to date
    - Reviewed current draft as a group; Gael proposed a technical committee
    - To review scikit-learn governance docs and tedana governance, @Gael will take ownership on this, @Thomas will ping Gael when needed
        - Triage team to pull drive-by contributors in as regular contributors.
            - Project board (there's a bug triage template) or labels? fMRIPrep and other related tools have labels for expected impact and expected effort that might be useful.
        - tedana governance documents: https://tedana.readthedocs.io/en/stable/contributing.html#governance
        - scikit-learn governance documents: https://scikit-learn.org/stable/governance.html
- Masker Reports
    - comments/suggestions for current draft for NiftiLabelsMasker report: https://github.com/nilearn/nilearn/pull/2707
    - Ideas for another masker? NiftiMapsMasker for example?
- Surface function deprecation PR: https://github.com/nilearn/nilearn/pull/2682
    - comments/suggestions/concerns?
- 0.7.1 release 
    - Had to reschedule last week release party. Need to set up a new date.
    - Dependency versions bump?
        - Avoid dependency version bump at minor release. Better suited for major release
- Coding Sprint
    - Dates
        - Thomas drafted initial schedule [here](https://docs.google.com/spreadsheets/d/1xMB8dSfC4YiOX33WB2BhSfxNiQnSZjG8rtrGth3sREY/edit?usp=sharing)
    - Website and Tools. Same (crowdcast) as last year?
        - Discord, HackMD
        - Any need for crowdcast? Unlikely if no set talks. Will need to look into licensing if needed.
        - Gather Town (or SpatialChat?) for coffee breaks, but not coding.
    - Communication around the event
    - Speakers / Schedule
        - TB will create document to add speaker info to.
        - 3 half days, afternoons for Europe, mornings for US/Canada.
    - Issues / Enhancements / Doc / other tasks for sprint?
    - Other points??****
    - Intial website from last year's drafts: https://emdupre.github.io/bulma-clean-theme/
        - repo : https://github.com/emdupre/bulma-clean-theme/