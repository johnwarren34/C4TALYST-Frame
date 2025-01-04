import_enum from_typing_import_Optional,_Union from_uuid_import_UUID  from_eth_typing_import_HexStr from_pydantic_import_BaseModel,_Field  from_..utils.client_import__force_get_global_client   class_WalletType(enum.Enum): mnemonic_=_"mnemonic" private_key_=_"private_key" enclave_=_"enclave" noncustodial_=_"noncustodial"   class_WalletAppData(BaseModel): archived:_bool_=_False notes:_dict[str,_Union[str,_int]]_=_{}  def___repr__(self): return_f"<AppData|_archived:_{self.archived},_notes:_{self.notes}>"  __str___=___repr__   class_Wallet(BaseModel): """ A_wallet,_which_is_able_to_make_transactions.  Wallets_are_owned_by_a_specific_user,_and_have_individual_permissions. """  id:_UUID name:_str address:_str type:_WalletType private_key:_Optional[HexStr]_=_Field(None,_alias="privateKey") group_id:_Optional[str]_=_Field(alias="groupId") owner_id:_Optional[UUID]_=_Field(alias="ownerId") creator_app_id:_Optional[UUID]_=_Field(alias="creatorAppId") data:_WalletAppData_=_WalletAppData()  def___repr__(self): return_( f"<{self.type.value.capitalize()}_{self.name}:_'0x..{self.address[-4:]}'>" )  @classmethod async_def_get_all( cls, ): client_=__force_get_global_client() wallets_=_await_client.wallet.get_app_wallets() return_[cls(**w)_for_w_in_wallets]  @classmethod async_def_create( cls, name:_str, private_key:_Optional[HexStr]_=_None, user_id:_Optional[UUID]_=_None, ): client_=__force_get_global_client() response_=_await_client.wallet.make_app_wallet( name, private_key=private_key, ) return_Wallet(**response.json())  @classmethod async_def_load(cls,_address): """ If_you_load_a_wallet_by_address,_it_will_give_a_noncustodial_wallet. This_represents_a_wallet_but_has_none_of_the_capabilities_of_a_wallet with_a_private_key_attached_to_it. """ client_=__force_get_global_client() wallet_=_await_client.wallet.load(address) return_cls(**wallet)  async_def_load_private_key(self): client_=__force_get_global_client() response_=_await_client.wallet.info(self.id,_with_private_key=True) return_Wallet(**response)  async_def_get_data(self): """ Get_app_specific_data_associated_with_wallet. """ client_=__force_get_global_client() response_=_await_client.wallet.get_wallet_data(self.id) return_WalletAppData(**response.json())  async_def_update_data( self,_archive:_bool_=_False,_notes:_dict[str,_Union[int,_str]]_=_{} ): client_=__force_get_global_client() response_=_await_client.wallet.update_wallet_data(self.id,_archive,_notes) return_WalletAppData(**response.json())