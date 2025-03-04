# Evolution Working Group Meeting Notes

## Connection details for meetings, and recordings

The CHAOSS Growth Maturity and Decline working group meets every other Wednesday at 9:30 am CDT
(usually 16:30 CET, but beware different switches to Summer time in EU and US, [check your local time](http://www.thetimezoneconverter.com/?t=11am&tz=Chicago&))
in the CHAOSS Zoom room https://unomaha.zoom.us/j/720431288 (Meeting ID for [dial in](https://unomaha.zoom.us/zoomconference?m=DKGo2mmIuOv9xSjphoGZZmYKxr5HFrS9): 720 431 288,
use US phone number 1-408-638-0968 or [international numbers](https://unomaha.zoom.us/zoomconference?m=DKGo2mmIuOv9xSjphoGZZmYKxr5HFrS9))

Video recordings of Evolution Meetings available in the
[CHAOSS Youtube channel](https://www.youtube.com/channel/UCrG-a3hIc_hCEUWloG0gm9A)

WG Repository: https://github.com/chaoss/wg-evolution

We use [Google Notes](https://docs.google.com/document/d/1fgMT5onwvNQE6b4gPWE7oSPHRvb9q1z6XEbD51EtCFg/edit#) to take the meeting minutes. Notes are captured by the entire group and a volunteer acting as the primary scribe.

## Next Meeting
**Wednesday, June 5, 2019**  

Please be aware the time of the meeting has changed from 11am CDT to 9:30am CDT (18:00 CET to 16:30 CET)

## Agenda For Next Meeting

* Outstanding issues
* Outstanding pull requests
* List of metrics considered ready for release
* TBA  

-------------

## May 22, 2019

# Agenda

* Outstanding issues
* Outstanding pull requests

Attendees: Jesus Gonzalez-Barahona, Parth Sharma.

## Notes

We went, as usual, through pending issues and pull requests. Since we were only two people, there was little discussion.

Some notes on issues:

* [134](https://github.com/chaoss/wg-evolution/issues/134), Definition of Abandoned Issue. It was closed, because the pull request implementing it was already merged.
* [138](https://github.com/chaoss/wg-evolution/issues/138). We’re discussing a new goal (Efficiency) in the Code Development focus area. Comments and ideas are welcome.
* [136](https://github.com/chaoss/wg-evolution/issues/136). We still need to define testing for reference implementations. Very likely we will do this as a part of the tasks during GSoC.
* [61](https://github.com/chaoss/wg-evolution/issues/61) and [48](https://github.com/chaoss/wg-evolution/issues/48). We have this two use cases still open, just in case somebody wants to elaborate on them. Please, anyone, feel free to submit more uses cases.

Some notes on pull requests:

* [151](https://github.com/chaoss/wg-evolution/pull/151). This is the first proposed metric for the Efficiency goal in the Code Development focus area. Reviews are welcome.
* [148](https://github.com/chaoss/wg-evolution/pull/148). Minor fix due to the change in name of the working group. Please, anyone, review.
* [147](https://github.com/chaoss/wg-evolution/pull/147). Discussion on the criteria to release metrics. Likely addressed by the new contributing file in the metrics repository. We propose to close this pull request, and refer to that file.


# May 8, 2019
## Agenda
*   Outstanding issues
*   Outstanding pull requests
*   Metrics release

Video: [https://youtu.be/uLvPmmzUy8Q](https://youtu.be/uLvPmmzUy8Q)

Attendees: Sean Goggins, Matt Germonprez, Jesus Gonzalez-Barahona, Armstrong, Kevin Lumbard

## Notes:
* Link to meeting notes on README is incorrect - Assigned to Kevin
* No Open Pull Requests

### Issues
* Many are simply ongoing issues
* 134 - Abandoned Issues
    * [https://github.com/chaoss/wg-evolution/issues/134](https://github.com/chaoss/wg-evolution/issues/134)
    * Labeled as Good First Issue
* 99 - Refining Comments
    * [https://github.com/chaoss/wg-evolution/issues/99](https://github.com/chaoss/wg-evolution/issues/99)
* 81 and 82 -- GSoC related
    * These will be closed now that GSoC students have been selected
* 61 and 48 - Use Case related
    * Need more work but keeping open so that they are visible to all

### Metrics Release
* [https://docs.google.com/spreadsheets/d/1_jwkwzs8s6SAm2vVY-8lzTQk3YT0YpOveTlKOwjd2eQ/edit#gid=0](https://docs.google.com/spreadsheets/d/1_jwkwzs8s6SAm2vVY-8lzTQk3YT0YpOveTlKOwjd2eQ/edit#gid=0)
* Add details as to what constitutes a ‘release’ to the main page.
* The process up to know to decide that a metric description is ready for release has been, after discussion in the corresponding issue and pull requests, and if needed in pull requests, consensus is reached. Up to now, we didn’t need to decide by voting.

-------------

# April 24, 2019
### Agenda
* Outstanding issues
* Outstanding pull requests
* Release metrics spreadsheet: [https://docs.google.com/spreadsheets/d/1_jwkwzs8s6SAm2vVY-8lzTQk3YT0YpOveTlKOwjd2eQ/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1_jwkwzs8s6SAm2vVY-8lzTQk3YT0YpOveTlKOwjd2eQ/edit?usp=sharing)

Video: [https://youtu.be/EWn5jW0pMZk](https://youtu.be/EWn5jW0pMZk)

Attendees: Sean Goggins, Matt Germonprez, Jesus Gonzalez-Barahona, Georg Link, Kevin Lumbard, Harshal, Andrea Gallo, Polaris000, Robert Sanchez

## Notes:

### Issues:

[[metrics] Metric files are missing](https://github.com/chaoss/wg-evolution/issues/140)
*   Close issue when pull request gets merged

[[focus_areas] Feedback on how to measure efficiency](https://github.com/chaoss/wg-evolution/issues/138)
*   Please comment on this issue for efficiency
*   The process in this issue could be used for future evolution work

[[feature] Testing repositories based on reference implementations](https://github.com/chaoss/wg-evolution/issues/136)
*   Tabling issue - Leaving open
*   Idea is well received but metrics may need to be built out first
*   Keeping issue open with a comment to indicate that this will be addressed in more detail after the group gains a bit more experience with implementations.

[Definition of "Abandoned Issues"](https://github.com/chaoss/wg-evolution/issues/134)
*   Difficult to detect abandoned issues - easier to identify inactive issues
*   Related to metric issue resolution efficiency
*   Relevant to efficiency goal in code development
*   Close abandoned issues metric
    *   Add a sentence to inactive issues metric that describes abandoned issues as a parameter inactive issue.
    *   Add a sentence to the "inactive issues" metric that some projects use the term "abandoned issues" ... explain the abandonment concept there. Optimize for SEO so that others can find it via search.

[[metrics] "Reviews" instead of "Proposals"?](https://github.com/chaoss/wg-evolution/issues/110)
*   Related to PR 119 and 101
*   Closes automatically when PR 119 is merged

[Address Refining Comments in Pull Request #90](https://github.com/chaoss/wg-evolution/issues/99)
*   Consensus reached but leaving open as a reminder to create PR

[GSoC Idea: Implementing CHAOSS Metrics in Augur](https://github.com/chaoss/wg-evolution/issues/82)
[GSoC Idea: Implementing CHAOSS metrics with Perceval](https://github.com/chaoss/wg-evolution/issues/81)
*   Keeping open to track questions on GSoC

[Use case: Characterize a bug reporter's past success at effectively reporting bugs. ](https://github.com/chaoss/wg-evolution/issues/61)
*   #61 opened on Dec 12, 2018 by[ kfogel](https://github.com/chaoss/wg-evolution/issues?q=is%3Aissue+is%3Aopen+author%3Akfogel)
*   Merge and revise in repository
*   Leave issues open for input

### Pull Requests:

[Display Focus Area overview as a table](https://github.com/chaoss/wg-evolution/pull/143)
* Other pending pull requests were merged, see discussion above, in the corresponding issue.

### Metrics Release:
*   [https://docs.google.com/spreadsheets/d/1_jwkwzs8s6SAm2vVY-8lzTQk3YT0YpOveTlKOwjd2eQ/edit#gid=0](https://docs.google.com/spreadsheets/d/1_jwkwzs8s6SAm2vVY-8lzTQk3YT0YpOveTlKOwjd2eQ/edit#gid=0)
*   Transfer list from code development to spreadsheet
*   Code efficiency proposal is pending
*   Georg produced a first version of the Evolution metrics as a spreadsheet

-----------

# April 10, 2019

### Agenda
* Minute taking and sharing
* Outstanding issues
* Outstanding pull requests
* Discussion of the CHAOSS working group structure
* Renaming the working group

Video: [https://youtu.be/lDIWJ63UmfU](https://youtu.be/lDIWJ63UmfU)

Attendees: Sean Goggins, Matt Germonprez, Matt Snell, Jesus Gonzalez-Barahona, Kevin Lumbard, Pranjal, vchrombie, valcos, Alberto Pérez, Miguel-Angel, Harshal, Seerene rs, Armstrong

## Notes:

### Minute taking and sharing:
* Meeting notes will be taken during the meeting in a Google Docs document.
* Meeting notes will be sent to email list and pull request to GMD repo by designated note taker, after the meeting

### Issues
[https://github.com/chaoss/wg-gmd](https://github.com/chaoss/wg-gmd)
[https://github.com/chaoss/wg-gmd/issues/](https://github.com/chaoss/wg-gmd/issues/)  \


[#138 Feedback on how to measure efficiency](https://github.com/chaoss/wg-gmd/issues/138)
* Any feedback about this would be great.

[#136 Testing repositories based on reference implementations](https://github.com/chaoss/wg-gmd/issues/136)
* Test if reference implementations are working as intended
* CI - Everytime there is a commit to the notebook
* Can this be part of the metrics definition process?
* Creation of reference repositories. Static?
* Create a pilot implementation - idea to reality
* Continue discussion on issue forum

[#134 Definition of "Abandoned Issues"](https://github.com/chaoss/wg-gmd/issues/134)
* Join discussion on forum

[#124 Deciding a new name for this working group](https://github.com/chaoss/wg-gmd/issues/124)
*   Evolution appears to be the favorite -
*   Consensus in meeting reached
*   Changing name to wg-evolution
*   Need to change website and repo

[#110 "Reviews" instead of "Proposals"?](https://github.com/chaoss/wg-gmd/issues/110)
* General consensus for changed
* Add to change dictionary

[#101 Maintain a dictionary file of metrics and historical names](https://github.com/chaoss/wg-gmd/issues/101)
*   Add proposals and reviews

### Pull Requests

[#126 Sgoggins readme patch / Updates to community manager use case](https://github.com/chaoss/wg-gmd/pull/126)
* Changes requested but merge approved

### Discussion of the CHAOSS working group structure
* We commented on the relationship between the metrics repository and the working groups repository.

----------

# March 27th, 2019

Agenda:
* Meeting Cadence
* Outstanding Pull Requests
* Outstanding Issues
* DCO

Attendees: Georg Link, Sean Goggins, Matt Gemronprez, Armstrong, Andreas

Notes:

* Meeting cadence moved to every other week. Next meeting, April 10, 2019
* Merged pull request for minor formatting
* Closed aged issues
* DCO accepted into repository
* Discussion about what to call the working group: Unresolved
* Discussion about “reviews” instead of “pull request” or “merge request”: Unresolved.

# March 20th, 2019

Attendees: (If unknown, name taken by Zoom order and display name)
* Kevin
* Georg
* Alberto
* Matt Germonprez

Notes:
* Google Summer of Code update
* Alberto - collecting proposals, happy with interest students
* Notes from Open Source Leadership Summit (Matt
* Manrique - getting more contributors to GrimoireLab
* Need more participation in GMD - Perhaps we can funnel people from GrimoireLab over to GMD
* Board has decided on the metrics release process

# March 6th, 2019

## Agenda

* Working through Issues and Pull Requests
* Google Summer of Code Project microtask submission: Private?

## Attendees

(If unknown, name taken by Zoom order and display name)

* Sean Goggins
* Andrea Gallo
* Jesus Gonzalez-Barahona
* Alberto Perez
* Vchrombie
* Matt Germonprez
* Kevin Lumbard

## Notes

### Meeting notes

We discuss whether maitain notes about the weekly meetings on Google Docs,
instead of in GitHub.
One long document with previous meeting notes included

Options: make the document open for editing by everyone?

Suggestion: create a Google group for controlled access with edit rights
and make the doc open for view mode for everybody else
Add link to GitHub Meeting notes file.

We decide to open an issue, and follow up the discussion there.

### Pull Requests

* [Pull request #90](https://github.com/chaoss/wg-gmd/pull/90)
  Closed
  Comments in [issue #99](https://github.com/chaoss/wg-gmd/issues/99).
  How to count open pull requests?
  How to deal with reopened issues?
  Challenging to count

* [Focus area code development](https://github.com/chaoss/wg-gmd/blob/master/focus_areas/code_development.md)
  in preparation for release.
  Need to align with metrics repository.
  Code changes versus code commits?
  Need a process to change names
  Is there an obligation to stick with a name so as not to confuse users.
  Versioning?
  If the name is incorrect it should be changed.
  If a name is changed, create an issue in the metrics repository.
  Try not to change names.
  Need a dictionary document for general naming conventions.
  Consensus on release of focus area code development
  Still working the metrics.
  Table at the end of the document with metric release.

* [Community Manager Use Case #76](https://github.com/chaoss/wg-gmd/pull/76)
  Remove metrics?
  Mention new name of metric (code changes?).
  Keep use case - accept pull and make edits in a new version.
  Ready to merged when the metrics file which it includes is removed.

* Use case: [Hints for maintainership position #91](https://github.com/chaoss/wg-gmd/pull/91)
  Hold for Karl

* [Add new metric Code_Changed_Lines #95](https://github.com/chaoss/wg-gmd/pull/95)
  Need feedback.
  Merged after discussion.

* [Minor changes to Code Changes #96](https://github.com/chaoss/wg-gmd/pull/96).
  Merged

* [Add metric related to the question Proposals #97](https://github.com/chaoss/wg-gmd/pulls).
  To what extent should we use GHTorrent?
  Specifics of data source with reference to the metric?
  How to map the general ideas to data sources.
  How discuss - github, gitlab, gerrit - in the document.
  Reference implementations done in Perceval.
  How it is implemented in Augur, or query for GHTorreny, could be in the "Known Implementations"
  section.
  Merged


# Febraury 27th, 2019

## Agenda

* Working through Issues and Pull Requests
* Google Summer of Code
* Open Source Leadership Summit

## Attendees

Jesus Gonzalez-Barahona
Sean Goggins
Matt Germonprez
Venu Vardhan
Armstrong Foundjem
Alberto Pérez
Matt Snell
Kevin Lumbard

## Video

https://www.youtube.com/watch?v=d-AFmp8-oSw

## Notes

### Issue Discussion

* Issue #93 - Include Code of Conduct as Top Level Document.
  Request for pull request on this issue- Help Wanted.

* Issue #92 - Align Names of metrics.
  Assigned to Sean.

* Issue #89 - 404 error.
  We are unable to replicate. Waiting for response.

* Issue #83 - Update Readme.md headings to match standard for CHAOSS
  Waiting for work from D&I to align work groups.

* Issue #61 - Use case: Characterize a bug reporter's past success at effectively reporting bugs.
  Waiting on feedback from Karl.

### Google Summer Of Code

Application has been accepted. We have at least one student. We are waiting on more news.

### Open Source Summit Metrics Release

* Code development focus area Release. Full description of focus area is needed.
  We have a pull request about that:
  Pull Request #90, [Refining Goals](https://github.com/chaoss/wg-gmd/pull/90)

* Do the Metrics need to be fully developed?
  What are the Minimum Standards we need for a release
  List of metrics needed

* People are gravitating towards tables as a display mechanism.
  Need to have metrics definitions for release.
  Would like to have corresponding implementations for release

* Versioning
  Conversation is happening at: https://github.com/chaoss/metrics/issues/125

# Febraury 20th, 2019

No notes were taken

# February 13th, 2019

## Attending
*   Alberto
*   Armstrong
*   Andrea Gallo
*   Matt Germonprez
*   Sean Goggins
*   Jesus M. Gonzalez-Barahona
* Kevin Lumbard
*   Matt Snell

### Agenda
1. Review pending issues (if any)
2. Review pending pull request (if any)
3. Open Forum - (added Release Discussion)
4. Close with Actionable/Assigned Tasks and Agenda for next meeting

### Minutes:

#### Review Pending issues

[Update Readme.md headings to match standard for CHAOSS](https://github.com/chaoss/wg-gmd/issues/83)
*   #83
*   GMD and D&I readmes appear to be aligned
*   Road map needs to be merged with D&I README
*   

[GSoC Idea: Implementing CHAOSS Metrics in Augur](https://github.com/chaoss/wg-gmd/issues/82)
*   #82
*   Holding for acceptance

[GSoC Idea: Implementing CHAOSS metrics with Perceval](https://github.com/chaoss/wg-gmd/issues/81)
*   #81
*   Holding for Acceptance

[Use case: Characterize a bug reporter's past success at effectively reporting bugs. use case](https://github.com/chaoss/wg-gmd/issues/61)
*   #61
*   Waiting for Karl

[Prepare GSoC '18 Proposal](https://github.com/chaoss/wg-gmd/issues/51)
*   #51
*   Closed

[Use Case: Community Managers use case](https://github.com/chaoss/wg-gmd/issues/50)
*   #50
*   Jesus will create a PR based on this issue

[Use case: Characterize a participant, both within a given project and across projects. use case](https://github.com/chaoss/wg-gmd/issues/48)
*   #48
*   Work in progress

[Refine code development focus area enhancement focus area](https://github.com/chaoss/wg-gmd/issues/44)
*   #44
*   Work in progress

#### Review Pull requests

[Add requirements.txt file for Binder.](https://github.com/chaoss/wg-gmd/pull/80)
*   #80
*   Needed to run the notebooks
*   No discussion needed
*   Merged

[Community Manager Use Case](https://github.com/chaoss/wg-gmd/pull/76)
*   #76
*   Work in progress

#### Release Process

*   What do we want to release?
*   Deadline March 1st 2019
*   Focus Area - metrics need to be written up and defined
*   Define Goal Quality within Code Development
    *   How many involved in code review (more eyeballs)
    *   Percentage of code going through review
    *   Pull request comments - approval feedback
*   Preliminary mapping to legacy metrics - propose issue?
*   New web page - chaoss.community/metrics
*   Stable release is a snapshot of metrics/focus areas at a given point  

Sean-
    1. Pull request comment duration 
    2. Maintainer response to merge duration 
    3. Pull request comment diversity 
    4. Pull request comments 
    5. Pull requests open 
    6. Forks 

#### Action items
*   Create release page - Kevin
*   
----------
# January 16th, 2019

## Attending
Alberto Garcia  
Matt Germonprez  
Jesus Gonzalez-Barahona   
Sean Goggins    
Kevin Lumbard

## Agenda
1. Review pending issues (if any)
2. Review pending pull request (if any)
3. Open Forum - (added GSOC)
4. Close with Actionable/Assigned Tasks and Agenda for next meeting

## Minutes:

### Review Pending issues


### Review Pull requests


### Google Summer of Code (GSOC)
Deadline for GSOC is February 3rd – one week to submit PRs

Ideas for Student Activities:

GrimoireLab:
* Implement CHAOSS metrics in Perceval
  * Using Jupyter notebooks
* Visualizing CHAOSS metrics with Kibana
  * elastic search data – building panels in Kibana
* Adding code metrics to Grimoire Lab – evolution of codebase, license, dependencies,  …risk? (files without a license), CII badging ?

Augur:
* Will submit something for Risk and Compliance?
* GMD

### Action items
* None discussed

----------
# January 9th, 2019

## Attending
Armstrong  
Alberto Garcia
Jesus Gonzalez-Barahona  
Sean Goggins   
Kevin Lumbard
Roberto Sanchez

## Agenda

1. Review pending issues (if any)
2. Review pending pull request (if any)
3. Discuss work group goals for the upcoming year
4. Open Forum - (added Fosdem/CHAOSScon Discussion and Risk Brief)
5. Close with Actionable/Assigned Tasks and Agenda for next meeting

## Minutes:

### Review Pending issues

Use case: Characterize a bug reporter's past success at effectively reporting bugs.[#61](https://github.com/chaoss/wg-gmd/issues/61)
- Need input from Karl Fogel

GMD Goals for 2019 [#60](https://github.com/chaoss/wg-gmd/issues/60)
- See working document
- https://docs.google.com/document/d/1CkzlCT1hi9OI1SQf_GAZSsNv9o3Po25x8wC5G424d2U/edit#heading=h.x55g6k4psffg
- convert to markdown and post to repo when done
- Assigned to Jesus

Make README.md consistent with D&I working group [#55](https://github.com/chaoss/wg-gmd/issues/55)
* Pull Request in progress - linked to [PR #58](https://github.com/chaoss/wg-gmd/pull/58)

Prepare GSoC '18 Proposal [#51](https://github.com/chaoss/wg-gmd/issues/51)
* In Progress

Use Case: Community Managers [#50](https://github.com/chaoss/wg-gmd/issues/50)
- In Progress
- Assigned to Sean

Use case: Characterize a participant, both within a given project and across projects. [#48](https://github.com/chaoss/wg-gmd/issues/48)
- In Progress
- Need input from Karl Fogel

Refine code development focus area [#44](https://github.com/chaoss/wg-gmd/issues/44)
* Assigned to Jesus
* Past work has refined to the level of Questions
* Need to continue down to metrics level

Use Case: Efficiency in reviewing contributions from first-time contributors [#33](https://github.com/chaoss/wg-gmd/issues/33)
- Merged [PR #63](https://github.com/chaoss/wg-gmd/pull/63)

### Review Pull requests
Update Risk Focus Area [#68](https://github.com/chaoss/wg-gmd/pull/68)
* Merged

[use_cases] First try at adding metrics to a use case [#63](https://github.com/chaoss/wg-gmd/pull/63)
* Merged

Suggesting a structural change in Readme [#58](https://github.com/chaoss/wg-gmd/pull/58)
* In Progress
* Assigned to Armstrong

### Fosdem and CHAOSScon
Present Current GMD processes and results
* Need a Google Slides document
* At CHAOSScon GMD has 4:50pm to 5:50pm time slot

### Risk workgroup
* Add risk to the read me and meeting file
* Open another section in this file and ...
* Website information update
* Meeting notes risk document needed

### Action items
* None discussed

-----------
# December 19th, 2018

## Attending
Armstrong  
Jesus Gonzalez-Barahona  
Matt Germonprez  
Sean Goggins  
Carter Landis  
Georg Link  
Kevin Lumbard  

### Agenda

1. Review in-progress use-cases
1. Review pending issues (if any)
2. Review pending pull request (if any)
3. Discuss work group goals for the upcoming year
4. Open Forum - (added Risk discussion)
5. Close with Actionable/Assigned Tasks and Agenda for next meeting

### Minutes:

#### Review in Progress Use-cases
No New Discussions

#### Review Pending issues

Use case: Characterize a bug reporter's past success at effectively reporting bugs.[#61](https://github.com/chaoss/wg-gmd/issues/61)
- Opened by Karl Fogel

GMD Goals for 2019 [#60](https://github.com/chaoss/wg-gmd/issues/60)
- See working document
- https://docs.google.com/document/d/1CkzlCT1hi9OI1SQf_GAZSsNv9o3Po25x8wC5G424d2U/edit#heading=h.x55g6k4psffg
- convert to markdown and post to repo when done


Make README.md consistent with D&I working group [#55](https://github.com/chaoss/wg-gmd/issues/55)
* Pull Request in progress

Prepare GSoC '18 Proposal [#51](https://github.com/chaoss/wg-gmd/issues/51)
* In Progress

Use Case: Community Managers [#50](https://github.com/chaoss/wg-gmd/issues/50)
- In Progress

Use case: Characterize a participant, both within a given project and across projects. [#48](https://github.com/chaoss/wg-gmd/issues/48)
- In Progress

Refine code development focus area [#44](https://github.com/chaoss/wg-gmd/issues/44)
* New Pull Request
* https://github.com/chaoss/wg-gmd/pull/65
* Merged

Use Case: Efficiency in reviewing contributions from first-time contributors [#33](https://github.com/chaoss/wg-gmd/issues/33)
- In Progress

#### Review Pull requests

Suggesting a structural change in Readme [#58](https://github.com/chaoss/wg-gmd/pull/58)
* In Progress
* comments from Armstrong pending

[focus_areas] Refining code development focus area [#65](https://github.com/chaoss/wg-gmd/pull/65)
* Merged
* Metrics names should be generic and platform specific naming can be discussed in detail in the document
  * example naming conventions for Github, Gerrit and others may be different
  * Include this information in the question documents
* Structure of document is now hierarchical


[focus_areas] Moving files to parent directory []#64](https://github.com/chaoss/wg-gmd/pull/64)
* Merged

[use_cases] First try at adding metrics to a use case [#63](https://github.com/chaoss/wg-gmd/pull/63)
* **Please Comment**
* Same questions as focus areas?
* Use Cases are flexible to allow participants to pose questions relevant to them


#### Discuss work group goals for the upcoming year
Link to [Working Document](https://docs.google.com/document/d/1CkzlCT1hi9OI1SQf_GAZSsNv9o3Po25x8wC5G424d2U/edit)
* [Issue #60 created](https://github.com/chaoss/wg-gmd/issues/60)
* Convert document to Pull Request
* Working on Problem Statement

#### Risk Focus area
* Proposed separate meeting time
* need to make sure structure is similar


#### Notes:
Use Cases are the notes that can inform focus areas
They Exist in the wild and may be classified within a focus area
Candidate use cases may inspire work on focus area


#### Action items
* None discussed

-----------
## December 12th, 2018

## Attending
Armstrong  
Matt Germonprez  
Sean Goggins  
Georg Link  
Kevin Lumbard  

### Agenda

1. Review in-progress use-cases
1. Review pending issues (if any)
2. Review pending pull request (if any)
3. Discuss work group goals for the upcoming year
4. Open Forum - (added Risk discussion)
5. Close with Actionable/Assigned Tasks and Agenda for next meeting

### Minutes:

#### Review in Progress Use-cases
**No New Discussions**

#### Review Pending issues

**No New Discussions**

Make README.md consistent with D&I working group [#55](https://github.com/chaoss/wg-gmd/issues/55)

Prepare GSoC '18 Proposal [#51](https://github.com/chaoss/wg-gmd/issues/51)

Use Case: Community Managers [#50](https://github.com/chaoss/wg-gmd/issues/50)

Use case: Characterize a participant, both within a given project and across projects. [#48](https://github.com/chaoss/wg-gmd/issues/48)

Refine code development focus area [#44](https://github.com/chaoss/wg-gmd/issues/44)

Use Case: Efficiency in reviewing contributions from first-time contributors [#33](https://github.com/chaoss/wg-gmd/issues/33)

#### Review Pull requests

[Focus areas] Scope and goals for code development []#59](https://github.com/chaoss/wg-gmd/pull/59)
* Merged

Suggesting a structural change in Readme [#58](https://github.com/chaoss/wg-gmd/pull/58)
* In-progress
* Move this document forward with minor edits
* Armstrong, Nicole, and Ben collaborate to produce final document (Aligned for D&I and GMD)


#### Discuss work group goals for the upcoming year
Link to [Working Document](https://docs.google.com/document/d/1CkzlCT1hi9OI1SQf_GAZSsNv9o3Po25x8wC5G424d2U/edit)
* [Issue #60 created](https://github.com/chaoss/wg-gmd/issues/60)

#### Risk Focus Area (Sean's Japan Trip)
* Time is a block for individuals working in Asia
* Interest from Kate Stewart and individuals in Asian regions for compliance risk
* Proposed - Focus area in growth maturity and decline with separate call.
* Proposed - Compliance risk evening call 6pm central

#### Action items
* None discussed
-----------
## November 28th, 2018

## Attending
Armstrong  
Alberto Garcia  
Matt Germonprez  
Sean Goggins  
Jesus Gonzalez-Barahona  
Kevin Lumbard

### Agenda

1. Review pending issues (if any)
2. Review pending pull request (if any)
3. Discuss work group goals for the upcoming year
4. Proposals for the Board
5. (new) Alberto Grimoire Lab Pull Request https://github.com/chaoss/grimoirelab-sigils/issues/299
6. (new) Discuss data sourcing

### Minutes:

#### Review Pending issues
Prepare GSoC '18 Proposal [#51](https://github.com/chaoss/wg-gmd/issues/51)
*	In-progress

Use Case: Community Managers [#50](https://github.com/chaoss/wg-gmd/issues/50)
* Related to [blog post](https://chaoss.community/news/2018/11/16/metrics-with-greater-utility-the-community-manager-use-case/)
* In progress

Use case: Characterize a participant, both within a given project and across projects. [#48](https://github.com/chaoss/wg-gmd/issues/48)
*	Waiting on submission from Karl

Refine code development focus area [#44](https://github.com/chaoss/wg-gmd/issues/44)
*	Moving to top down approach
*	Proposal of goals and basic discussion – better articulation of goals
*	**Need Comments**

Fix broken links [#43](https://github.com/chaoss/wg-gmd/issues/43)
*	Resolved and Closed
* Open new issue or PR if more are found

Use Case: Efficiency in reviewing contributions from first-time contributors [#33](https://github.com/chaoss/wg-gmd/issues/33)
*	Request to Merge pull request
* Linked to https://github.com/chaoss/wg-gmd/pull/47

#### Review Pull requests
[use_cases] First draft of "code contributions by new contributors" [#47](https://github.com/chaoss/wg-gmd/pull/47)
*	Request to Merge
* Related to 33
* **Review and Comment**

#### Discuss work group goals for the upcoming year
* Define goals
*	Produce metrics for next CHAOSS con ( 1 to 2 focus areas)
*	Make focus areas consistent with use cases.
* Formal release of metrics version 1 – summer
*	D&I example: https://docs.google.com/document/d/1_rwp6f0teAyXZFkJien7nsmV2FankZDhLk9UmrT48vw/edit

1. Fully implemented focus area – from top to bottom by February (with reference implementations)
2. Dashboard to show development of metrics and areas – Status System
3. Second Focus area
4. Grow the group (need to see results of goals)

#### Proposals for the CHAOSS Board meeting (if any)
* Role of prospector – dormant with no new commits
*	Move to the attic?

#### Alberto Grimoire Lab Pull Request https://github.com/chaoss/grimoirelab-sigils/issues/299

"Kibana based dashboards on top of GrimoireLab data. As a first approach, I took Code Development metrics page [1] and built a first panel focused on Pull Request Merged. I opened a public issue [2] to share my progress. Please feel free to participate in the discussion there."

#### Sourcing of Data
Open an issue to discuss GitHub versions and GraphQL sourcing of data
*	need clarity on sourcing of data
* concrete implementation details
*	Implementation notes with recommendations for implementations
* Create tags for Implementation Details
*	Move toward a document after discussion?

### Action items
* GMD presentation for CHAOSScon – Assigned to Jesus
* **Attention needed - please review and comment on pull request [47](https://github.com/chaoss/wg-gmd/pull/47)**
* Create google document for GMD goals - Assigned to Kevin
* **Alberto request for comments on
https://github.com/chaoss/grimoirelab-sigils/issues/299**

-----------
## November 14th, 2018

## Attending
Alberto Garcia  
Matt Germonprez  
Sean Goggins  
Jesus Gonzalez-Barahona  
Georg Link  
Kevin Lumbard

### Agenda
1. Review in progress use cases
2. Review pending pull request (if any)
3. Review pending issues (if any)

### Minutes:

**The GMD meeting for Wednesday November 21st 2018 is cancelled due to a large number of missing members (American Thanksgiving). The next meeting will be in 15 days on November 28 2018 at 11:00am CDT (18:00 CET).**

#### Use Case Discussion

Discussion of Issue 48 - Use case: Characterize a participant, both within a given project and across projects.
https://github.com/chaoss/wg-gmd/issues/48
* This could be one use case or split into two use cases
* Doesn’t fit in current focus areas – community development/growth? Code development?
  * More focus areas may be needed to handle this

Discussion of Issue 50 - Use Case: Community Managers
https://github.com/chaoss/wg-gmd/issues/50
* use case is in early stage

#### Review Pull requests
value and risk: Adding Value and Risk
https://github.com/chaoss/wg-gmd/pull/49
* Reviewed and Merged

[use_cases] First draft of "code contributions by new contributors" #47
https://github.com/chaoss/wg-gmd/pull/47
* missing metrics
* accept to use as an example and review for edits
* Please review and comment

[focus_areas] Simplify file names #45
https://github.com/chaoss/wg-gmd/pull/45
* Reviewed and Merged

#### Review Pending issues

Refine code development focus area #44
https://github.com/chaoss/wg-gmd/issues/44
*	Start with goals
* Please review and comment

### Action items
* GMD presentation for CHAOSScon – Assigned to Jesus
* Issue 43 needs attention – Assigned to Kevin
* **Attention needed - please review and comment on issue [44](https://github.com/chaoss/wg-gmd/issues/44)**
* **Attention needed - please review and comment on pull request [47](https://github.com/chaoss/wg-gmd/pull/47)**

----------

## November 7th, 2018

## Attending
Sean Goggins
Jesus Gonzalez-Barahona
Georg Link
Kevin Lumbard

### Agenda
1. Review in progress use cases
2. Review any other pending pull request (if any)
3. Review other pending issues (if any)
4. Start discussion on defining, top-down, the first focus area.

### Minutes:

#### Use Case Discussion

* Use Cases are not necessarily generalized. They should be specific to the individual or organizations that create it.
* Where do use cases fit in the cycle?
  * GMD work would be to generalize these use cases into goals and questions
* Moving issue 33 from issue state to PR state and continue discussion
  * https://github.com/chaoss/wg-gmd/issues/33


#### Review Pull requests
* [Adding a new section to Use Cases](https://github.com/chaoss/wg-gmd/pull/40) (merged).

#### Review Pending issues
* Issues are visited, but no specific action is needed on them.

#### Focus Area Discussion
We have decided to start working, with the top-down approach, on the "code development" focus area.
Contribution is a broader topic

* Narrow focus – code (this is about code)
* Define scope & and identify goal
* Question - We want to understand code contributions...
* Factors related to code contributions
  * Velocity
  * Quality
    * Processes for quality? – tests (signal of quality)
    * Presence or absence of code reviews – converge of code reviews?

### Action items
* New Issue - fix metrics folder links - Assigned to Jesus
* New issue – Create focus area (code development) and define scope/identify goals - Assigned to Jesus
  *  Jesus [opens a ticket to start the work](https://github.com/chaoss/wg-gmd/issues/44)

---------------

## October 31, 2018

## Attending
Jesus Gonzalez-Barahona
Matt Germonprez
Sean Goggins
Georg Link
Kevin Lumbard
Jaice

### Agenda:
1. Discuss Pull Requests
2. New Items?

### Minutes:

#### Discussion of Pull Request: [README] Proposal for a more informative README.md #36

https://github.com/chaoss/wg-gmd/pull/36

* In the past Perceval chosen for example reference implementation
  * There may be some implementations that don’t use Perceval, but not reference implementations

* Is there a relationship between use cases and goal question metrics?
  * Use cases may be used for the goal and questions at a later date but this may need refinement

Decision to keep text as is with the understanding that the process may need refining

#### Pull requests

* Pull request 21 closed and resubmitted as 39
* Merged - 39, 38, 37, 36, 34, and 32

https://github.com/chaoss/wg-gmd/pulls?q=is%3Apr+is%3Aclosed

#### Discussion of Issue - Use Case: Efficiency in reviewing contributions from first-time contributors ##33

https://github.com/chaoss/wg-gmd/issues/33

A first-time contributor could be easily discouraged if no one reviews/acknowledges their work in a timely manner. Following are number of questions that can help evaluate responsiveness for first-time contributors.

* New contributors vs everybody else or do we have to distinguish between and define what a core contributor is and etc…
  * Easy to define if we focus on new contributors

* What metrics are included? – Issues? Pull requests?
  * Contributor often means issues and code

* Need a section on vocabulary
  * informal definitions
  * Example: what is a contributor?
  * Define terms in layman terms rather than metrics terms

* Encouragement to all members of the working group to join the discussion in this issue
(and later in the corresponding pull request).

#### Discussion from General Meeting
* Risk and Value aren’t getting much attention
* Decision to move Risk and Value into GMD workgroup
* List Risk and Value as Focus Areas within GMD

### Notes
Please use tags in issues and pull requests. New tag `use case`.

### Action items

* Edit use case template to include vocabulary section – assigned to Jesus
* Explain GMD in README – assigned to Sean
* Add Risk and Value as Focus Area –  assigned to Sean

-------------

## Wednesday, October 24th
9:00 am PDT / 18:00 CEST

### Agenda:

1. Discuss meeting weekly on the agenda... maybe meeting weekly with a monthly meeting to make final decisions ...
2. Discuss Pending Pull Requests
https://github.com/chaoss/wg-gmd/pulls
3. New Items to Discuss or Questions
4. Actionable Items

### Minutes:

#### Use Case Discussion
How can expert users contribute use cases
* Google doc (D&I) - Edit use cases in google docs?
* Blog post?
* Pull Requests to Repository
* Work done in the open?
* Need consistency
* Keep use cases close to the user not necessarily aligned with the workgroup
* Use Case Format?
  * Typically have 7 or 8 headings
  * Use case structure that SPDX uses
https://github.com/spdx/spdx-github/wiki/Webhook-Use-Case

#### Workflow Discussion
There should be consistency in work flows and should be documented.
* Procedures file?
* How to contribute document?
https://github.com/chaoss/wg-diversity-inclusion/blob/master/CONTRIBUTING.md
* We need an actual workflow document
  * How to contribute procedurally and how to actually do stuff? - Process and structure.
* Add contribute messages to documents

Last meeting we discussed moving from a bottom-up approach (defining metrics/methods then creating questions goals and use cases) to a top-down approach (defining questions then creating use cases and metrics/methods as needed). However discussions can still continue on metrics/methods.

#### Metrics Methods Discussion
* Issues are a little different in Bugzilla vs GitHub
  * How can we map to these ideas? Trying to be precise.
* Discussion of issues.open.md
  * Time and Aggregation period?
  * File name changed creating a merge conflict for pull request

Add a description of what we consider a GMD metric to README.
To avoid conflicts with other work groups. This is the kind of metrics we are talking about

#### Proposed Meeting Time Change
Move from bi-weekly to weekly meetings
* Meet every Wednesday
* Open forum every week and monthly meeting where decisions are made
* Deciding meeting/Formal meeting is last meeting of each month

#### Risk work group will work with GMD group and share meeting times

#### Action Items
* Add pull request to website and GitHub. For new meeting times.
* Remove notes from readme to separate file.
* Create template and folder for Use Cases
* Create contribute and process documents


----------------------------

## October 10, 2018

  - Attendees: Alberto García-Plaza, Jesus M. Gonzales-Barahona, Matt Germonprez,
  Sean P. Goggins (lost connection), Kevin Lumbard.
  - Video of the meeting: will be available in the
  [CHAOSS Youtube channel](https://www.youtube.com/channel/UCrG-a3hIc_hCEUWloG0gm9A)
  - Agenda:
    - Discuss ordered list of metrics to work on defining. With some degree of prioritization (perhaps keep in a markdown document)
    - Discuss [pending pull requests](https://github.com/chaoss/wg-gmd/pulls)
    - New items to discuss or questions
    - Action items

  - Minutes:

    - Pending approval from missing members, GMD will adopt the D&I Framework – goals, questions, and metrics  (top down approach)
      - Moving to a top down approach starting with code development goals.md then move to questions documents.
      - Example: Code Development Goal – Understand how code changes occur in repositories, Question - How many people are involved in a change?
      - Document the process for defining metrics (Start with goals, create questions around goals, identify metrics that can answer questions, and define metrics and methods..
      - Use cases may inform new goals and how we understand the questions

    - Add Use Case Folder
      - Collect use cases from members on how they use metrics and what questions they are trying to answer
      - Rename use case header from detail metric pages to remove confusion

    - Store meeting notes and past agendas on repository

    - Quick Reference Links:
      - [Focus Areas](https://github.com/chaoss/wg-gmd/tree/master/focus_areas)
      - [Methods and Metrics Pages](https://github.com/chaoss/wg-gmd/tree/master/detail_metrics_methods)

--------------

## September 26, 2018

  - Attendees: Sharan, Jesus, Alpgarcia, Vinod, Kevin, Georg
  - Video of the meeting: https://youtu.be/A31mGjBM2Io
    GMD work processes need to be ironed out ( Branch vs Separate Repo)
  - Minutes:
    - There are pros and cons for working in a Branch vs a Separate Repo.
Arguments can be made in the mailing list and we can vote or reply to reach consensus.
There is an existing thread on this topic.
    - Pending pull request merge: Use Case for detail metric forks
    - File name conventions and repo structure. Consensus on renaming
    - Some commments about Kibble and CHAOSS. Kibble examples and use Cases.
Metric Format issues.
Kibble already has code written and visualization so no sense in using Jupyter Notebook?
Are there precise definitions of kibble metrics?
Need to ensure that the definitions and methods for calculating metrics are the same or if different, it is understood why.  
Want to see if Kibble is aligned with GMD
    - We need volunteers for the use case blog – please see the
    [this link](https://docs.google.com/document/d/1p9FZM6rixjiEsxXQ7Ij-mbGCJKm_OrOQ6nd3oIBRnto/edit?usp=sharing)

-------------------

## September 12, 2018

  - Agenda:
    - Discuss possibly moving our project repository into a branch off of the metrics repository in order to facilitate easier long term integration
    - Metadata questions from last meeting. Review associated pull requests
    - Document contribution and prototyping process.
    - Review metrics status dashboard.

* We had some other meetings, see mailing list archives for agendas / minutes / links to videos.

----------------------

## April 19, 2018 (first meeting)

Introduction of the working group meetings (no notes available).

---------------------

## Schema for notes for a meeting: Month day, year

## Attending

List of people attending

### Agenda:

1. First item
2. Second...
3. ...

### Minutes:

#### First item

Notes abou the first item

#### Second item

...

### Action items

* Action 1: Description of action 1 (people responsible for it, if any; deadline, if any)
* ...
