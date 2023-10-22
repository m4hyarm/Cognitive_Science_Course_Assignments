#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on March 06, 2022, at 19:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'id': '810100476', 'handedness': '', 'eyeness': '', 'gender': '', 'age': '', 'edujation': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['id'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\MAHYAR\\Desktop\\UT py\\CS py\\HW1\\test\\test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "hi"
hiClock = core.Clock()
hello = visual.TextStim(win=win, name='hello',
    text='سلام',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);

# Initialize components for Routine "tutorial"
tutorialClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None, anchor='center',
    ori=90.0, pos=(0, 0), size=(0.7, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()
upper_text = visual.TextStim(win=win, name='upper_text',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
lower_text = visual.TextStim(win=win, name='lower_text',
    text='- در صورت آماده بودن کلید Space را فشار دهید -',
    font='Open Sans',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-3.0);

# Initialize components for Routine "count_down"
count_downClock = core.Clock()
var_3 = visual.TextStim(win=win, name='var_3',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
var_2 = visual.TextStim(win=win, name='var_2',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
var_1 = visual.TextStim(win=win, name='var_1',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fix_point"
fix_pointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.02, 0.02), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "faces"
facesClock = core.Clock()
stim = visual.ImageStim(
    win=win,
    name='stim', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "key_press"
key_pressClock = core.Clock()
ky_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "hi"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
hiComponents = [hello]
for thisComponent in hiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = hiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hello* updates
    if hello.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hello.frameNStart = frameN  # exact frame index
        hello.tStart = t  # local t and not account for scr refresh
        hello.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hello, 'tStartRefresh')  # time at next scr refresh
        hello.setAutoDraw(True)
    if hello.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > hello.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            hello.tStop = t  # not accounting for scr refresh
            hello.frameNStop = frameN  # exact frame index
            win.timeOnFlip(hello, 'tStopRefresh')  # time at next scr refresh
            hello.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hi"-------
for thisComponent in hiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('hello.started', hello.tStartRefresh)
thisExp.addData('hello.stopped', hello.tStopRefresh)

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=4.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Book2.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "tutorial"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_2.setImage(pic)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    upper_text.setText(txt)
    # keep track of which components have finished
    tutorialComponents = [image_2, key_resp, upper_text, lower_text]
    for thisComponent in tutorialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    tutorialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tutorial"-------
    while continueRoutine:
        # get current time
        t = tutorialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=tutorialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *upper_text* updates
        if upper_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upper_text.frameNStart = frameN  # exact frame index
            upper_text.tStart = t  # local t and not account for scr refresh
            upper_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upper_text, 'tStartRefresh')  # time at next scr refresh
            upper_text.setAutoDraw(True)
        
        # *lower_text* updates
        if lower_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lower_text.frameNStart = frameN  # exact frame index
            lower_text.tStart = t  # local t and not account for scr refresh
            lower_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lower_text, 'tStartRefresh')  # time at next scr refresh
            lower_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tutorialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tutorial"-------
    for thisComponent in tutorialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('image_2.started', image_2.tStartRefresh)
    blocks.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    blocks.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        blocks.addData('key_resp.rt', key_resp.rt)
    blocks.addData('key_resp.started', key_resp.tStartRefresh)
    blocks.addData('key_resp.stopped', key_resp.tStopRefresh)
    blocks.addData('upper_text.started', upper_text.tStartRefresh)
    blocks.addData('upper_text.stopped', upper_text.tStopRefresh)
    blocks.addData('lower_text.started', lower_text.tStartRefresh)
    blocks.addData('lower_text.stopped', lower_text.tStopRefresh)
    # the Routine "tutorial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "count_down"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    count_downComponents = [var_3, var_2, var_1]
    for thisComponent in count_downComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    count_downClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "count_down"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = count_downClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=count_downClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *var_3* updates
        if var_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            var_3.frameNStart = frameN  # exact frame index
            var_3.tStart = t  # local t and not account for scr refresh
            var_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(var_3, 'tStartRefresh')  # time at next scr refresh
            var_3.setAutoDraw(True)
        if var_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > var_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                var_3.tStop = t  # not accounting for scr refresh
                var_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(var_3, 'tStopRefresh')  # time at next scr refresh
                var_3.setAutoDraw(False)
        
        # *var_2* updates
        if var_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            var_2.frameNStart = frameN  # exact frame index
            var_2.tStart = t  # local t and not account for scr refresh
            var_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(var_2, 'tStartRefresh')  # time at next scr refresh
            var_2.setAutoDraw(True)
        if var_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > var_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                var_2.tStop = t  # not accounting for scr refresh
                var_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(var_2, 'tStopRefresh')  # time at next scr refresh
                var_2.setAutoDraw(False)
        
        # *var_1* updates
        if var_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            var_1.frameNStart = frameN  # exact frame index
            var_1.tStart = t  # local t and not account for scr refresh
            var_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(var_1, 'tStartRefresh')  # time at next scr refresh
            var_1.setAutoDraw(True)
        if var_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > var_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                var_1.tStop = t  # not accounting for scr refresh
                var_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(var_1, 'tStopRefresh')  # time at next scr refresh
                var_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in count_downComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "count_down"-------
    for thisComponent in count_downComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('var_3.started', var_3.tStartRefresh)
    blocks.addData('var_3.stopped', var_3.tStopRefresh)
    blocks.addData('var_2.started', var_2.tStartRefresh)
    blocks.addData('var_2.stopped', var_2.tStopRefresh)
    blocks.addData('var_1.started', var_1.tStartRefresh)
    blocks.addData('var_1.stopped', var_1.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    each_hand = data.TrialHandler(nReps=2.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Book1.xlsx'),
        seed=None, name='each_hand')
    thisExp.addLoop(each_hand)  # add the loop to the experiment
    thisEach_hand = each_hand.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEach_hand.rgb)
    if thisEach_hand != None:
        for paramName in thisEach_hand:
            exec('{} = thisEach_hand[paramName]'.format(paramName))
    
    for thisEach_hand in each_hand:
        currentLoop = each_hand
        # abbreviate parameter names if possible (e.g. rgb = thisEach_hand.rgb)
        if thisEach_hand != None:
            for paramName in thisEach_hand:
                exec('{} = thisEach_hand[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix_point"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_pointComponents = [polygon]
        for thisComponent in fix_pointComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_pointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_point"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fix_pointClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_pointClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_pointComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_point"-------
        for thisComponent in fix_pointComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        each_hand.addData('polygon.started', polygon.tStartRefresh)
        each_hand.addData('polygon.stopped', polygon.tStopRefresh)
        
        # ------Prepare to start Routine "faces"-------
        continueRoutine = True
        routineTimer.add(0.050000)
        # update component parameters for each repeat
        stim.setPos(poss)
        stim.setSize(size)
        stim.setImage(stm)
        # keep track of which components have finished
        facesComponents = [stim]
        for thisComponent in facesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        facesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "faces"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = facesClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=facesClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stim* updates
            if stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stim.frameNStart = frameN  # exact frame index
                stim.tStart = t  # local t and not account for scr refresh
                stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
                stim.setAutoDraw(True)
            if stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    stim.tStop = t  # not accounting for scr refresh
                    stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim, 'tStopRefresh')  # time at next scr refresh
                    stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in facesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "faces"-------
        for thisComponent in facesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        each_hand.addData('stim.started', stim.tStartRefresh)
        each_hand.addData('stim.stopped', stim.tStopRefresh)
        
        # ------Prepare to start Routine "key_press"-------
        continueRoutine = True
        # update component parameters for each repeat
        ky_2.keys = []
        ky_2.rt = []
        _ky_2_allKeys = []
        # keep track of which components have finished
        key_pressComponents = [ky_2]
        for thisComponent in key_pressComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        key_pressClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "key_press"-------
        while continueRoutine:
            # get current time
            t = key_pressClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=key_pressClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ky_2* updates
            waitOnFlip = False
            if ky_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ky_2.frameNStart = frameN  # exact frame index
                ky_2.tStart = t  # local t and not account for scr refresh
                ky_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ky_2, 'tStartRefresh')  # time at next scr refresh
                ky_2.status = STARTED
                # AllowedKeys looks like a variable named `key`
                if not type(key) in [list, tuple, np.ndarray]:
                    if not isinstance(key, str):
                        logging.error('AllowedKeys variable `key` is not string- or list-like.')
                        core.quit()
                    elif not ',' in key:
                        key = (key,)
                    else:
                        key = eval(key)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ky_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ky_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ky_2.status == STARTED and not waitOnFlip:
                theseKeys = ky_2.getKeys(keyList=list(key), waitRelease=False)
                _ky_2_allKeys.extend(theseKeys)
                if len(_ky_2_allKeys):
                    ky_2.keys = _ky_2_allKeys[-1].name  # just the last key pressed
                    ky_2.rt = _ky_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in key_pressComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "key_press"-------
        for thisComponent in key_pressComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if ky_2.keys in ['', [], None]:  # No response was made
            ky_2.keys = None
        each_hand.addData('ky_2.keys',ky_2.keys)
        if ky_2.keys != None:  # we had a response
            each_hand.addData('ky_2.rt', ky_2.rt)
        each_hand.addData('ky_2.started', ky_2.tStartRefresh)
        each_hand.addData('ky_2.stopped', ky_2.tStopRefresh)
        # the Routine "key_press" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'each_hand'
    
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'blocks'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
