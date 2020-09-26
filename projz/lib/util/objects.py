class UserProfile:
    def __init__(self, data):
        self.json = data

        try: self.tagList = TagList(data["tagList"]).TagList
        except (KeyError, TypeError): self.tagList = None

        self.userId = None
        self.status = None
        self.email = None
        self.createdTime = None
        self.hasProfile = None
        self.deviceId = None
        self.nickname = None
        self.socialId = None
        self.socialIdModified = None
        self.gender = None
        self.icon = None
        self.iconUrl = None
        self.chatInvitationStatus = None
        self.contentRegion = None
        self.contentRegionName = None
        self.showsLocation = None
        self.nameCardEnabled = None
        self.language = None
        self.showsSchool = None
        self.school = None
        self.pushEnabled = None
        self.showsJoinedCircles = None
        self.birthday = None
        self.bio = None
        self.onlineStatus = None
        self.chatMemberStatus = None
        self.location = None
        self.nameCardBackground = None
        self.fansCount = None
        self.followingCount = None
        self.friendsCount = None
        self.followMeStatus = None
        self.followedByMeStatus = None
        self.specialTitle = None
        self.longitude = None
        self.latitude = None
        self.address = None

    @property
    def UserProfile(self):
        try: self.userId = self.json["uid"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.email = self.json["email"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.hasProfile = self.json["hasProfile"]
        except (KeyError, TypeError): pass
        try: self.deviceId = self.json["deviceId"]
        except (KeyError, TypeError): pass
        try: self.nickname = self.json["nickname"]
        except (KeyError, TypeError): pass
        try: self.socialId = self.json["socialId"]
        except (KeyError, TypeError): pass
        try: self.socialIdModified = self.json["socialIdModified"]
        except (KeyError, TypeError): pass
        try: self.gender = self.json["gender"]
        except (KeyError, TypeError): pass
        try: self.icon = self.json["icon"]
        except (KeyError, TypeError): pass
        try: self.iconUrl = self.json["icon"]["baseUrl"]
        except (KeyError, TypeError): pass
        try: self.chatInvitationStatus = self.json["chatInvitationStatus"]
        except (KeyError, TypeError): pass
        try: self.contentRegion = self.json["contentRegion"]
        except (KeyError, TypeError): pass
        try: self.contentRegionName = self.json["contentRegionName"]
        except (KeyError, TypeError): pass
        try: self.showsLocation = self.json["showsLocation"]
        except (KeyError, TypeError): pass
        try: self.nameCardEnabled = self.json["nameCardEnabled"]
        except (KeyError, TypeError): pass
        try: self.language = self.json["language"]
        except (KeyError, TypeError): pass
        try: self.showsSchool = self.json["showsSchool"]
        except (KeyError, TypeError): pass
        try: self.school = self.json["school"]
        except (KeyError, TypeError): pass
        try: self.pushEnabled = self.json["pushEnabled"]
        except (KeyError, TypeError): pass
        try: self.showsJoinedCircles = self.json["showsJoinedCircles"]
        except (KeyError, TypeError): pass
        try: self.birthday = self.json["birthday"]
        except (KeyError, TypeError): pass
        try: self.bio = self.json["bio"]
        except (KeyError, TypeError): pass
        try: self.onlineStatus = self.json["onlineStatus"]
        except (KeyError, TypeError): pass
        try: self.chatMemberStatus = self.json["chatMemberStatus"]
        except (KeyError, TypeError): pass
        try: self.location = self.json["location"]
        except (KeyError, TypeError): pass
        try: self.nameCardBackground = self.json["nameCardBackground"]
        except (KeyError, TypeError): pass
        try: self.fansCount = self.json["fansCount"]
        except (KeyError, TypeError): pass
        try: self.friendsCount = self.json["friendsCount"]
        except (KeyError, TypeError): pass
        try: self.followingCount = self.json["followingCount"]
        except (KeyError, TypeError): pass
        try: self.followMeStatus = self.json["followMeStatus"]
        except (KeyError, TypeError): pass
        try: self.followedByMeStatus = self.json["followedByMeStatus"]
        except (KeyError, TypeError): pass
        try: self.specialTitle = self.json["specialTitle"]
        except (KeyError, TypeError): pass
        try: self.longitude = self.json["location"]["longitude"]
        except (KeyError, TypeError): pass
        try: self.latitude = self.json["location"]["latitude"]
        except (KeyError, TypeError): pass
        try: self.address = self.json["location"]["address"]
        except (KeyError, TypeError): pass

        return self

class UserProfileList:
    def __init__(self, data):
        _tagList = []
        self.json = data

        for obj_ in data:
            try: _tagList.append(TagList(obj_["tagList"]).TagList)
            except (KeyError, TypeError): _tagList.append(None)

        self.tagList = _tagList
        self.userId = []
        self.status = []
        self.email = []
        self.createdTime = []
        self.hasProfile = []
        self.deviceId = []
        self.nickname = []
        self.socialId = []
        self.socialIdModified = []
        self.gender = []
        self.icon = []
        self.iconUrl = []
        self.chatInvitationStatus = []
        self.contentRegion = []
        self.contentRegionName = []
        self.showsLocation = []
        self.nameCardEnabled = []
        self.language = []
        self.showsSchool = []
        self.school = []
        self.pushEnabled = []
        self.showsJoinedCircles = []
        self.birthday = []
        self.bio = []
        self.onlineStatus = []
        self.chatMemberStatus = []
        self.location = []
        self.nameCardBackground = []
        self.fansCount = []
        self.followingCount = []
        self.friendsCount = []
        self.followMeStatus = []
        self.followedByMeStatus = []
        self.specialTitle = []
        self.longitude = []
        self.latitude = []
        self.address = []

    @property
    def UserProfileList(self):
        for obj in self.json:
            try: self.userId.append(obj["uid"])
            except (KeyError, TypeError): self.userId.append(None)
            try: self.status.append(obj["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.email.append(obj["email"])
            except (KeyError, TypeError): self.email.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.hasProfile.append(obj["hasProfile"])
            except (KeyError, TypeError): self.hasProfile.append(None)
            try: self.deviceId.append(obj["deviceId"])
            except (KeyError, TypeError): self.deviceId.append(None)
            try: self.nickname.append(obj["nickname"])
            except (KeyError, TypeError): self.nickname.append(None)
            try: self.socialId.append(obj["socialId"])
            except (KeyError, TypeError): self.socialId.append(None)
            try: self.socialIdModified.append(obj["socialIdModified"])
            except (KeyError, TypeError): self.socialIdModified.append(None)
            try: self.gender.append(obj["gender"])
            except (KeyError, TypeError): self.gender.append(None)
            try: self.icon.append(obj["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.iconUrl.append(obj["icon"]["baseUrl"])
            except (KeyError, TypeError): self.iconUrl.append(None)
            try: self.chatInvitationStatus.append(obj["chatInvitationStatus"])
            except (KeyError, TypeError): self.chatInvitationStatus.append(None)
            try: self.contentRegion.append(obj["contentRegion"])
            except (KeyError, TypeError): self.contentRegion.append(None)
            try: self.contentRegionName.append(obj["contentRegionName"])
            except (KeyError, TypeError): self.contentRegionName.append(None)
            try: self.showsLocation.append(obj["showsLocation"])
            except (KeyError, TypeError): self.showsLocation.append(None)
            try: self.nameCardEnabled.append(obj["nameCardEnabled"])
            except (KeyError, TypeError): self.nameCardEnabled.append(None)
            try: self.language.append(obj["language"])
            except (KeyError, TypeError): self.language.append(None)
            try: self.showsSchool.append(obj["showsSchool"])
            except (KeyError, TypeError): self.showsSchool.append(None)
            try: self.school.append(obj["school"])
            except (KeyError, TypeError): self.school.append(None)
            try: self.pushEnabled.append(obj["pushEnabled"])
            except (KeyError, TypeError): self.pushEnabled.append(None)
            try: self.showsJoinedCircles.append(obj["showsJoinedCircles"])
            except (KeyError, TypeError): self.showsJoinedCircles.append(None)
            try: self.birthday.append(obj["birthday"])
            except (KeyError, TypeError): self.birthday.append(None)
            try: self.bio.append(obj["bio"])
            except (KeyError, TypeError): self.bio.append(None)
            try: self.onlineStatus.append(obj["onlineStatus"])
            except (KeyError, TypeError): self.onlineStatus.append(None)
            try: self.chatMemberStatus.append(obj["chatMemberStatus"])
            except (KeyError, TypeError): self.chatMemberStatus.append(None)
            try: self.location.append(obj["location"])
            except (KeyError, TypeError): self.location.append(None)
            try: self.nameCardBackground.append(obj["nameCardBackground"])
            except (KeyError, TypeError): self.nameCardBackground.append(None)
            try: self.fansCount.append(obj["fansCount"])
            except (KeyError, TypeError): self.fansCount.append(None)
            try: self.followingCount.append(obj["followingCount"])
            except (KeyError, TypeError): self.followingCount.append(None)
            try: self.friendsCount.append(obj["friendsCount"])
            except (KeyError, TypeError): self.friendsCount.append(None)
            try: self.followingCount.append(obj["followingCount"])
            except (KeyError, TypeError): self.followingCount.append(None)
            try: self.followMeStatus.append(obj["followMeStatus"])
            except (KeyError, TypeError): self.followMeStatus.append(None)
            try: self.followedByMeStatus.append(obj["followedByMeStatus"])
            except (KeyError, TypeError): self.followedByMeStatus.append(None)
            try: self.specialTitle.append(obj["specialTitle"])
            except (KeyError, TypeError): self.specialTitle.append(None)
            try: self.longitude.append(obj["location"]["longitude"])
            except (KeyError, TypeError): self.longitude.append(None)
            try: self.latitude.append(obj["location"]["latitude"])
            except (KeyError, TypeError): self.latitude.append(None)
            try: self.address.append(obj["location"]["address"])
            except (KeyError, TypeError): self.address.append(None)

        return self

class GetBlogs:
    def __init__(self, data):
        self.json = data

        try: self.blog = BlogList(data["list"]).BlogList
        except (KeyError, TypeError): self.blog = None

        self.nextPageToken = None

    @property
    def GetBlogs(self):
        try: self.nextPageToken = self.json["pagination"]["nextPageToken"]
        except (KeyError, TypeError): pass

        return self

class GetChats:
    def __init__(self, data):
        self.json = data

        try: self.chat = ChatList(data["list"]).ChatList
        except (KeyError, TypeError): self.chat = None

        self.nextPageToken = None
        self.isEnd = None
        self.threadCheckList = None

    @property
    def GetChats(self):
        try: self.nextPageToken = self.json["pagination"]["nextPageToken"]
        except (KeyError, TypeError): pass
        try: self.isEnd = self.json["isEnd"]
        except (KeyError, TypeError): pass
        try: self.threadCheckList = self.json["threadCheckList"]
        except (KeyError, TypeError): pass

        return self

class Blog:
    def __init__(self, data):
        self.json = data

        try: self.author = UserProfile(data["author"]).UserProfile
        except (KeyError, TypeError): self.author = None
        try: self.tagList = TagList(data["tagList"]).TagList
        except (KeyError, TypeError): self.tagList = None
        try: self.circleList = CircleList(data["circleList"]).CircleList
        except (KeyError, TypeError): self.circleList = None

        self.blogId = None
        self.circleIdList = None
        self.createdTime = None
        self.status = None
        self.type = None
        self.authorId = None
        self.content = None
        self.mediaList = None
        self.votesCount = None
        self.commentsCount = None
        self.extensions = None
        self.contentRegion = None
        self.language = None

    @property
    def Blog(self):
        try: self.blogId = self.json["blogId"]
        except (KeyError, TypeError): pass
        try: self.circleIdList = self.json["circleIdList"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.type = self.json["type"]
        except (KeyError, TypeError): pass
        try: self.authorId = self.json["uid"]
        except (KeyError, TypeError): pass
        try: self.content = self.json["content"]
        except (KeyError, TypeError): pass
        try: self.mediaList = self.json["mediaList"]
        except (KeyError, TypeError): pass
        try: self.votesCount = self.json["votesCount"]
        except (KeyError, TypeError): pass
        try: self.commentsCount = self.json["commentsCount"]
        except (KeyError, TypeError): pass
        try: self.extensions = self.json["extensions"]
        except (KeyError, TypeError): pass
        try: self.contentRegion = self.json["contentRegion"]
        except (KeyError, TypeError): pass
        try: self.language = self.json["language"]
        except (KeyError, TypeError): pass

        return self

class BlogList:
    def __init__(self, data):
        _author, _tagList, _circleList = [], [], []
        self.json = data

        for obj_ in data:
            try: _author.append(obj_["author"])
            except (KeyError, TypeError): _author.append(None)
            try: _tagList.append(TagList(obj_["tagList"]).TagList)
            except (KeyError, TypeError): _tagList.append(None)
            try: _circleList.append(CircleList(obj_["circleList"]).CircleList)
            except (KeyError, TypeError): _circleList.append(None)

        self.author = UserProfileList(_author).UserProfileList
        self.tagList = _tagList
        self.circleList = _circleList
        self.blogId = []
        self.circleIdList = []
        self.createdTime = []
        self.status = []
        self.type = []
        self.authorId = []
        self.content = []
        self.mediaList = []
        self.votesCount = []
        self.commentsCount = []
        self.extensions = []
        self.contentRegion = []
        self.language = []

    @property
    def BlogList(self):
        for obj in self.json:
            try: self.blogId.append(obj["blogId"])
            except (KeyError, TypeError): self.blogId.append(None)
            try: self.circleIdList.append(obj["circleIdList"])
            except (KeyError, TypeError): self.circleIdList.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.status.append(obj["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.type.append(obj["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.authorId.append(obj["uid"])
            except (KeyError, TypeError): self.authorId.append(None)
            try: self.content.append(obj["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.mediaList.append(obj["mediaList"])
            except (KeyError, TypeError): self.mediaList.append(None)
            try: self.votesCount.append(obj["votesCount"])
            except (KeyError, TypeError): self.votesCount.append(None)
            try: self.commentsCount.append(obj["commentsCount"])
            except (KeyError, TypeError): self.commentsCount.append(None)
            try: self.extensions.append(obj["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.contentRegion.append(obj["contentRegion"])
            except (KeyError, TypeError): self.contentRegion.append(None)
            try: self.language.append(obj["language"])
            except (KeyError, TypeError): self.language.append(None)

        return self

class Chat:
    def __init__(self, data):
        self.json = data

        try: self.host = UserProfile(data["host"]).UserProfile
        except (KeyError, TypeError): self.host = None
        try: self.membersSummary = UserProfileList(data["membersSummary"]).UserProfileList
        except (KeyError, TypeError): self.membersSummary = None
        try: self.latestMessage = Message(data["latestMessage"]).Message
        except (KeyError, TypeError): self.latestMessage = None

        self.chatId = None
        self.status = None
        self.type = None
        self.hostId = None
        self.coHostIds = None
        self.title = None
        self.icon = None
        self.iconUrl = None
        self.content = None
        self.latestMessageId = None
        self.membersCount = None
        self.background = None
        self.backgroundUrl = None
        self.contentRegion = None
        self.createdTime = None
        self.language = None
        self.extensions = None
        self.activityType = None
        self.rolePlayMode = None
        self.alertOption = None
        self.currentMemberInfo = None

    @property
    def Chat(self):
        try: self.chatId = self.json["threadId"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.type = self.json["type"]
        except (KeyError, TypeError): pass
        try: self.hostId = self.json["hostUid"]
        except (KeyError, TypeError): pass
        try: self.coHostIds = self.json["coHostUids"]
        except (KeyError, TypeError): pass
        try: self.title = self.json["title"]
        except (KeyError, TypeError): pass
        try: self.icon = self.json["icon"]
        except (KeyError, TypeError): pass
        try: self.iconUrl = self.json["icon"]["baseUrl"]
        except (KeyError, TypeError): pass
        try: self.content = self.json["content"]
        except (KeyError, TypeError): pass
        try: self.latestMessageId = self.json["latestMessageId"]
        except (KeyError, TypeError): pass
        try: self.membersCount = self.json["membersCount"]
        except (KeyError, TypeError): pass
        try: self.background = self.json["background"]
        except (KeyError, TypeError): pass
        try: self.backgroundUrl = self.json["background"]["baseUrl"]
        except (KeyError, TypeError): pass
        try: self.contentRegion = self.json["contentRegion"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.language = self.json["language"]
        except (KeyError, TypeError): pass
        try: self.extensions = self.json["extensions"]
        except (KeyError, TypeError): pass
        try: self.activityType = self.json["extensions"]["activityType"]
        except (KeyError, TypeError): pass
        try: self.rolePlayMode = self.json["extensions"]["rolePlayMode"]
        except (KeyError, TypeError): pass
        try: self.alertOption = self.json["currentMemberInfo"]["alertOption"]
        except (KeyError, TypeError): pass
        try: self.currentMemberInfo = self.json["currentMemberInfo"]
        except (KeyError, TypeError): pass

        return self

class ChatList:
    def __init__(self, data):
        _host, _membersSummary, _latestMessage = [], [], []
        self.json = data

        for obj_ in data:
            try: _host.append(obj_["host"])
            except (KeyError, TypeError): _host.append(None)
            try: _membersSummary.append(UserProfileList(obj_["membersSummary"]).UserProfileList)
            except (KeyError, TypeError): _membersSummary.append(None)
            try: _latestMessage.append(obj_["latestMessage"])
            except (KeyError, TypeError): _latestMessage.append(None)

        self.host = UserProfileList(_host).UserProfileList
        self.membersSummary = _membersSummary
        self.latestMessage = MessageList(_latestMessage).MessageList
        self.chatId = []
        self.status = []
        self.type = []
        self.hostId = []
        self.coHostIds = []
        self.title = []
        self.icon = []
        self.iconUrl = []
        self.content = []
        self.latestMessageId = []
        self.membersCount = []
        self.background = []
        self.backgroundUrl = []
        self.contentRegion = []
        self.createdTime = []
        self.language = []
        self.extensions = []
        self.activityType = []
        self.rolePlayMode = []
        self.alertOption = []
        self.currentMemberInfo = []

    @property
    def ChatList(self):
        for obj in self.json:
            try: self.chatId.append(obj["threadId"])
            except (KeyError, TypeError): self.chatId.append(None)
            try: self.status.append(obj["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.type.append(obj["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.hostId.append(obj["hostUid"])
            except (KeyError, TypeError): self.hostId.append(None)
            try: self.coHostIds.append(obj["coHostUids"])
            except (KeyError, TypeError): self.coHostIds.append(None)
            try: self.title.append(obj["title"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.icon.append(obj["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.iconUrl.append(obj["icon"]["baseUrl"])
            except (KeyError, TypeError): self.iconUrl.append(None)
            try: self.content.append(obj["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.latestMessageId.append(obj["latestMessageId"])
            except (KeyError, TypeError): self.latestMessageId.append(None)
            try: self.membersCount.append(obj["membersCount"])
            except (KeyError, TypeError): self.membersCount.append(None)
            try: self.background.append(obj["background"])
            except (KeyError, TypeError): self.background.append(None)
            try: self.backgroundUrl.append(obj["background"]["baseUrl"])
            except (KeyError, TypeError): self.backgroundUrl.append(None)
            try: self.contentRegion.append(obj["contentRegion"])
            except (KeyError, TypeError): self.contentRegion.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.language.append(obj["language"])
            except (KeyError, TypeError): self.language.append(None)
            try: self.extensions.append(obj["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.activityType.append(obj["extensions"]["activityType"])
            except (KeyError, TypeError): self.activityType.append(None)
            try: self.rolePlayMode.append(obj["extensions"]["rolePlayMode"])
            except (KeyError, TypeError): self.rolePlayMode.append(None)
            try: self.alertOption.append(obj["currentMemberInfo"]["alertOption"])
            except (KeyError, TypeError): self.alertOption.append(None)
            try: self.currentMemberInfo.append(obj["currentMemberInfo"])
            except (KeyError, TypeError): self.currentMemberInfo.append(None)

        return self

class Message:
    def __init__(self, data):
        self.json = data

        try: self.author = UserProfile(data["author"]).UserProfile
        except (KeyError, TypeError): self.author = None
        try: self.role = Role(data["role"]).Role
        except (KeyError, TypeError): self.role = None
        try: self.userList = UserProfileList(data["userList"]).UserProfileList
        except (KeyError, TypeError): self.userList = None

        self.content = None
        self.messageId = None
        self.chatId = None
        self.authorId = None
        self.createdTime = None
        self.type = None
        self.asSummary = None
        self.extensions = None
        self.friendshipLevel = None
        self.roleId = None
        self.invitedIds = None

    @property
    def Message(self):
        try: self.content = self.json["content"]
        except (KeyError, TypeError): pass
        try: self.messageId = self.json["messageId"]
        except (KeyError, TypeError): pass
        try: self.chatId = self.json["threadId"]
        except (KeyError, TypeError): pass
        try: self.authorId = self.json["uid"]
        except (KeyError, TypeError): pass
        try: self.type = self.json["type"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.asSummary = self.json["asSummary"]
        except (KeyError, TypeError): pass
        try: self.extensions = self.json["extensions"]
        except (KeyError, TypeError): pass
        try: self.friendshipLevel = self.json["extensions"]["friendshipLevel"]
        except (KeyError, TypeError): pass
        try: self.roleId = self.json["extensions"]["roleId"]
        except (KeyError, TypeError): pass
        try: self.invitedIds = self.json["extensions"]["invitedUids"]
        except (KeyError, TypeError): pass

        return self

class MessageList:
    def __init__(self, data):
        _author, _role, _userList = [], [], []
        self.json = data

        for obj_ in data:
            try: _author.append(obj_["author"])
            except (KeyError, TypeError): _author.append(None)
            try: _role.append(obj_["role"])
            except (KeyError, TypeError): _role.append(None)
            try: _userList.append(UserProfileList(obj_["userList"]).UserProfileList)
            except (KeyError, TypeError): _userList.append(None)

        self.author = UserProfileList(_author).UserProfileList
        self.userList = _userList
        self.role = RoleList(_role).RoleList
        self.content = []
        self.messageId = []
        self.chatId = []
        self.authorId = []
        self.createdTime = []
        self.type = []
        self.asSummary = []
        self.extensions = []
        self.friendshipLevel = []
        self.roleId = []
        self.invitedIds = []

    @property
    def MessageList(self):
        for obj in self.json:
            try: self.content.append(obj["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.messageId.append(obj["messageId"])
            except (KeyError, TypeError): self.messageId.append(None)
            try: self.chatId.append(obj["threadId"])
            except (KeyError, TypeError): self.chatId.append(None)
            try: self.authorId.append(obj["uid"])
            except (KeyError, TypeError): self.authorId.append(None)
            try: self.type.append(obj["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.asSummary.append(obj["asSummary"])
            except (KeyError, TypeError): self.asSummary.append(None)
            try: self.extensions.append(obj["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.friendshipLevel.append(obj["extensions"]["friendshipLevel"])
            except (KeyError, TypeError): self.friendshipLevel.append(None)
            try: self.roleId.append(obj["extensions"]["roleId"])
            except (KeyError, TypeError): self.roleId.append(None)
            try: self.invitedIds.append(obj["extensions"]["invitedUids"])
            except (KeyError, TypeError): self.invitedIds.append(None)

        return self

class Circle:
    def __init__(self, data):
        self.json = data

        try: self.author = UserProfile(data["author"]).UserProfile
        except (KeyError, TypeError): self.author = None
        try: self.tagList = TagList(data["tagList"]).TagList
        except (KeyError, TypeError): self.tagList = None

        self.name = None
        self.description = None
        self.circleId = None
        self.tagline = None
        self.socialId = None
        self.createdTime = None
        self.status = None
        self.language = None
        self.contentRegion = None
        self.membersCount = None
        self.icon = None
        self.iconUrl = None
        self.joinedStatus = None
        self.authorId = None
        self.background = None
        self.backgroundUrl = None
        self.socialIdModified = None
        self.adminIdList = None

    @property
    def Circle(self):
        try: self.name = self.json["name"]
        except (KeyError, TypeError): pass
        try: self.circleId = self.json["circleId"]
        except (KeyError, TypeError): pass
        try: self.tagline = self.json["tagline"]
        except (KeyError, TypeError): pass
        try: self.socialId = self.json["socialId"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.language = self.json["language"]
        except (KeyError, TypeError): pass
        try: self.contentRegion = self.json["contentRegion"]
        except (KeyError, TypeError): pass
        try: self.membersCount = self.json["membersCount"]
        except (KeyError, TypeError): pass
        try: self.icon = self.json["icon"]
        except (KeyError, TypeError): pass
        try: self.iconUrl = self.json["icon"]["baseUrl"]
        except (KeyError, TypeError): pass
        try: self.joinedStatus = self.json["joinedStatus"]
        except (KeyError, TypeError): pass
        try: self.authorId = self.json["uid"]
        except (KeyError, TypeError): pass
        try: self.background = self.json["background"]
        except (KeyError, TypeError): pass
        try: self.backgroundUrl = self.json["background"]["baseUrl"]
        except (KeyError, TypeError): pass
        try: self.description = self.json["description"]
        except (KeyError, TypeError): pass
        try: self.socialIdModified = self.json["socialIdModified"]
        except (KeyError, TypeError): pass
        try: self.adminIdList = self.json["adminIdList"]
        except (KeyError, TypeError): pass

        return self

class CircleList:
    def __init__(self, data):
        _author, _tagList = [], []
        self.json = data

        for obj_ in data:
            try: _author.append(obj_["author"])
            except (KeyError, TypeError): _author.append(None)
            try: _tagList = TagList(obj_["tagList"]).TagList
            except (KeyError, TypeError): _tagList.append(None)

        self.author = UserProfileList(_author).UserProfileList
        self.tagList = _tagList
        self.name = []
        self.description = []
        self.circleId = []
        self.tagline = []
        self.socialId = []
        self.createdTime = []
        self.status = []
        self.language = []
        self.contentRegion = []
        self.membersCount = []
        self.icon = []
        self.iconUrl = []
        self.joinedStatus = []
        self.authorId = []
        self.background = []
        self.backgroundUrl = []
        self.socialIdModified = []
        self.adminIdList = []

    @property
    def CircleList(self):
        for obj in self.json:
            try: self.name.append(obj["name"])
            except (KeyError, TypeError): self.name.append(None)
            try: self.circleId.append(obj["circleId"])
            except (KeyError, TypeError): self.circleId.append(None)
            try: self.tagline.append(obj["tagline"])
            except (KeyError, TypeError): self.tagline.append(None)
            try: self.socialId.append(obj["socialId"])
            except (KeyError, TypeError): self.socialId.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.status.append(obj["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.language.append(obj["language"])
            except (KeyError, TypeError): self.language.append(None)
            try: self.contentRegion.append(obj["contentRegion"])
            except (KeyError, TypeError): self.contentRegion.append(None)
            try: self.membersCount.append(obj["membersCount"])
            except (KeyError, TypeError): self.membersCount.append(None)
            try: self.icon.append(obj["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.iconUrl.append(obj["icon"]["baseUrl"])
            except (KeyError, TypeError): self.iconUrl.append(None)
            try: self.joinedStatus.append(obj["joinedStatus"])
            except (KeyError, TypeError): self.joinedStatus.append(None)
            try: self.authorId.append(obj["uid"])
            except (KeyError, TypeError): self.authorId.append(None)
            try: self.background.append(obj["background"])
            except (KeyError, TypeError): self.background.append(None)
            try: self.backgroundUrl.append(obj["background"]["baseUrl"])
            except (KeyError, TypeError): self.backgroundUrl.append(None)
            try: self.description.append(obj["description"])
            except (KeyError, TypeError): self.description.append(None)
            try: self.socialIdModified.append(obj["socialIdModified"])
            except (KeyError, TypeError): self.socialIdModified.append(None)
            try: self.adminIdList.append(obj["adminIdList"])
            except (KeyError, TypeError): self.adminIdList.append(None)

        return self

class CommentList:
    def __init__(self, data):
        _author, _subComments = [], []
        self.json = data

        for obj_ in data:
            try: _author.append(obj_["author"])
            except (KeyError, TypeError): _author.append(None)
            try: _subComments.append(CommentList(obj_["subComments"]).CommentList)
            except (KeyError, TypeError): _subComments.append(None)

        self.author = UserProfileList(_author).UserProfileList
        self.subComments = _subComments
        self.commentId = []
        self.createdTime = []
        self.parentId = []
        self.parentType = []
        self.uid = []
        self.circleId = []
        self.replyId = []
        self.status = []
        self.content = []
        self.type = []
        self.subCommentsCount = []
        self.votesCount = []
        self.votedValue = []
        self.replyToId = []
        self.extensions = []
        self.contentStatus = []
        self.replyToUser = []

    @property
    def CommentList(self):
        for obj in self.json:
            try: self.commentId.append(obj["commentId"])
            except (KeyError, TypeError): self.commentId.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.parentId.append(obj["parentId"])
            except (KeyError, TypeError): self.parentId.append(None)
            try: self.parentType.append(obj["parentType"])
            except (KeyError, TypeError): self.parentType.append(None)
            try: self.uid.append(obj["uid"])
            except (KeyError, TypeError): self.uid.append(None)
            try: self.circleId.append(obj["circleId"])
            except (KeyError, TypeError): self.circleId.append(None)
            try: self.replyId.append(obj["replyId"])
            except (KeyError, TypeError): self.replyId.append(None)
            try: self.status.append(obj["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.content.append(obj["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.type.append(obj["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.subCommentsCount.append(obj["subCommentsCount"])
            except (KeyError, TypeError): self.subCommentsCount.append(None)
            try: self.votesCount.append(obj["votesCount"])
            except (KeyError, TypeError): self.votesCount.append(None)
            try: self.votedValue.append(obj["votedValue"])
            except (KeyError, TypeError): self.votedValue.append(None)
            try: self.extensions.append(obj["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.replyToId.append(obj["extensions"]["replyToUid"])
            except (KeyError, TypeError): self.replyToId.append(None)
            try: self.contentStatus.append(obj["extensions"]["contentStatus"])
            except (KeyError, TypeError): self.contentStatus.append(None)
            try: self.replyToUser.append(UserProfile(obj["extensions"]["replyToUser"]).UserProfile)
            except (KeyError, TypeError): self.replyToUser.append(None)

        return self

class AlertsList:
    def __init__(self, data):
        _operator = []
        self.json = data

        for obj_ in data:
            try: _operator.append(obj_["operator"])
            except (KeyError, TypeError): _operator.append(None)

        self.operator = UserProfileList(_operator).UserProfileList
        self.alertId = []
        self.operatorId = []
        self.targetId = []
        self.circleId = []
        self.createdTime = []
        self.groupId = []
        self.type = []
        self.objectId = []
        self.objectType = []
        self.objectText = []
        self.parentId = []
        self.parentType = []
        self.parentText = []
        self.contextText = []
        self.circleInfo = []

    @property
    def AlertsList(self):
        for obj in self.json:
            try: self.alertId.append(obj["alertId"])
            except (KeyError, TypeError): self.alertId.append(None)
            try: self.operatorId.append(obj["operatorUid"])
            except (KeyError, TypeError): self.operatorId.append(None)
            try: self.targetId.append(obj["targetUid"])
            except (KeyError, TypeError): self.targetId.append(None)
            try: self.circleId.append(obj["circleId"])
            except (KeyError, TypeError): self.circleId.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.groupId.append(obj["groupId"])
            except (KeyError, TypeError): self.groupId.append(None)
            try: self.type.append(obj["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.objectId.append(obj["objectId"])
            except (KeyError, TypeError): self.objectId.append(None)
            try: self.objectType.append(obj["objectType"])
            except (KeyError, TypeError): self.objectType.append(None)
            try: self.objectText.append(obj["objectText"])
            except (KeyError, TypeError): self.objectText.append(None)
            try: self.parentId.append(obj["parentId"])
            except (KeyError, TypeError): self.parentId.append(None)
            try: self.parentType.append(obj["parentType"])
            except (KeyError, TypeError): self.parentType.append(None)
            try: self.parentText.append(obj["parentText"])
            except (KeyError, TypeError): self.parentText.append(None)
            try: self.contextText.append(obj["contextText"])
            except (KeyError, TypeError): self.contextText.append(None)
            try: self.circleInfo.append(obj["circleInfo"])
            except (KeyError, TypeError): self.circleInfo.append(None)

        return self

class AlertsInfo:
    def __init__(self, data):
        self.json = data
        self.activitiesAlertCount = None
        self.likesAlertCount = None
        self.followersAlertCount = None
        self.noticesCount = None

    @property
    def AlertsInfo(self):
        try: self.activitiesAlertCount = self.json["activitiesAlertCount"]
        except (KeyError, TypeError): pass
        try: self.likesAlertCount = self.json["likesAlertCount"]
        except (KeyError, TypeError): pass
        try: self.followersAlertCount = self.json["followersAlertCount"]
        except (KeyError, TypeError): pass
        try: self.noticesCount = self.json["noticesCount"]
        except (KeyError, TypeError): pass

        return self

class ContentRegionList:
    def __init__(self, data):
        self.json = data
        self.contentRegion = []
        self.contentRegionName = []

    @property
    def ContentRegionList(self):
        for obj in self.json:
            try: self.contentRegion.append(obj["contentRegion"])
            except (KeyError, TypeError): self.contentRegion.append(None)
            try: self.contentRegionName.append(obj["contentRegionName"])
            except (KeyError, TypeError): self.contentRegionName.append(None)

        return self

class Tag:
    def __init__(self, data):
        self.json = data
        self.name = None
        self.lowerCaseName = None
        self.tagId = None
        self.source = None
        self.status = None
        self.order = None
        self.style = None
        self.type = None
        self.languageCode = None
        self.backgroundColor = None
        self.borderColor = None
        self.solidColor = None
        self.createdTime = None

    @property
    def Tag(self):
        try: self.name = self.json["tagName"]
        except (KeyError, TypeError): pass
        try: self.lowerCaseName = self.json["lowerCaseName"]
        except (KeyError, TypeError): pass
        try: self.tagId = self.json["tagId"]
        except (KeyError, TypeError): pass
        try: self.source = self.json["source"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.order = self.json["order"]
        except (KeyError, TypeError): pass
        try: self.style = self.json["style"]
        except (KeyError, TypeError): pass
        try: self.backgroundColor = self.json["style"]["backgroundColor"]
        except (KeyError, TypeError): pass
        try: self.borderColor = self.json["style"]["borderColor"]
        except (KeyError, TypeError): pass
        try: self.solidColor = self.json["style"]["solidColor"]
        except (KeyError, TypeError): pass
        try: self.type = self.json["tagType"]
        except (KeyError, TypeError): pass
        try: self.languageCode = self.json["languageCode"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass

        return self

class TagList:
    def __init__(self, data):
        self.json = data
        self.name = []
        self.lowerCaseName = []
        self.tagId = []
        self.source = []
        self.status = []
        self.order = []
        self.style = []
        self.type = []
        self.languageCode = []
        self.backgroundColor = []
        self.borderColor = []
        self.solidColor = []
        self.createdTime = []

    @property
    def TagList(self):
        for obj in self.json:
            try: self.name.append(obj["tagName"])
            except (KeyError, TypeError): self.name.append(None)
            try: self.lowerCaseName.append(obj["lowerCaseName"])
            except (KeyError, TypeError): self.lowerCaseName.append(None)
            try: self.tagId.append(obj["tagId"])
            except (KeyError, TypeError): self.tagId.append(None)
            try: self.source.append(obj["source"])
            except (KeyError, TypeError): self.source.append(None)
            try: self.status.append(obj["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.order.append(obj["order"])
            except (KeyError, TypeError): self.order.append(None)
            try: self.style.append(obj["style"])
            except (KeyError, TypeError): self.style.append(None)
            try: self.backgroundColor.append(obj["style"]["backgroundColor"])
            except (KeyError, TypeError): self.backgroundColor.append(None)
            try: self.borderColor.append(obj["style"]["borderColor"])
            except (KeyError, TypeError): self.borderColor.append(None)
            try: self.solidColor.append(obj["style"]["solidColor"])
            except (KeyError, TypeError): self.solidColor.append(None)
            try: self.type.append(obj["tagType"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.languageCode.append(obj["languageCode"])
            except (KeyError, TypeError): self.languageCode.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)

        return self

class Share:
    def __init__(self, data):
        self.json = data
        self.path = None
        self.objectId = None
        self.objectType = None
        self.shareLink = None

    @property
    def Share(self):
        try: self.path = self.json["path"]
        except (KeyError, TypeError): pass
        try: self.objectId = self.json["objectId"]
        except (KeyError, TypeError): pass
        try: self.objectType = self.json["objectType"]
        except (KeyError, TypeError): pass
        try: self.shareLink = self.json["shareLink"]
        except (KeyError, TypeError): pass

        return self

class Role:
    def __init__(self, data):
        self.json = data
        self.name = None
        self.chatId = None
        self.roleId = None
        self.authorId = None
        self.icon = None
        self.iconUrl = None
        self.description = None
        self.createdTime = None
        self.inUse = None

    @property
    def Role(self):
        try: self.name = self.json["name"]
        except (KeyError, TypeError): pass
        try: self.chatId = self.json["threadId"]
        except (KeyError, TypeError): pass
        try: self.roleId = self.json["roleId"]
        except (KeyError, TypeError): pass
        try: self.authorId = self.json["uid"]
        except (KeyError, TypeError): pass
        try: self.icon = self.json["icon"]
        except (KeyError, TypeError): pass
        try: self.iconUrl = self.json["icon"]["baseUrl"]
        except (KeyError, TypeError): pass
        try: self.description = self.json["description"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.inUse = self.json["inUse"]
        except (KeyError, TypeError): pass

        return self

class RoleList:
    def __init__(self, data):
        self.json = data
        self.name = []
        self.chatId = []
        self.roleId = []
        self.authorId = []
        self.icon = []
        self.iconUrl = []
        self.description = []
        self.createdTime = []
        self.inUse = []

    @property
    def RoleList(self):
        for obj in self.json:
            try: self.name.append(obj["name"])
            except (KeyError, TypeError): self.name.append(None)
            try: self.chatId.append(obj["threadId"])
            except (KeyError, TypeError): self.chatId.append(None)
            try: self.roleId.append(obj["roleId"])
            except (KeyError, TypeError): self.roleId.append(None)
            try: self.authorId.append(obj["uid"])
            except (KeyError, TypeError): self.authorId.append(None)
            try: self.icon.append(obj["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.iconUrl.append(obj["icon"]["baseUrl"])
            except (KeyError, TypeError): self.iconUrl.append(None)
            try: self.description.append(obj["description"])
            except (KeyError, TypeError): self.description.append(None)
            try: self.createdTime.append(obj["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.inUse.append(obj["inUse"])
            except (KeyError, TypeError): self.inUse.append(None)

        return self